"""Append AOC correction cycles to date-wise CSV files."""

import csv
import os
import zipfile
from datetime import datetime
from threading import Lock
from xml.sax.saxutils import escape


CSV_DIRECTORY = "/home/torizon/app/data/Octo_CSV"
USB_MOUNT_DIRECTORY = "/media"
CSV_HEADER = [
    "Sr.No",
    "Program_id",
    "Partname",
    "Dimension",
    "Job count",
    "Machine",
    "Tool_no",
    "Nominal",
    "Readings",
    "Correction",
    "Tool_value",
    "date",
    "time",
]
_csv_lock = Lock()

class AOCExport:
    """Writes AOC correction records to the daily CSV file."""

    def export_to_csv(
            self,
            Sr_No,
            Program_id,
            Partname,
            Dimension,
            Job_count,
            Machine,
            Tool_no,
            Nominal,
            Readings,
            Correction,
            Tool_value,
        ):
            """
            Save one AOC correction cycle to the daily CSV file.

            CSV format:
            Sr.No, Program_id, partname, dimension,job count,Machine, tool_no, nominal,
            reading, correction, tool_value,  date, time
            """
            try:
                now = datetime.now()

                csv_path = os.path.join(
                    CSV_DIRECTORY,
                    "aoc_corrections_{}.csv".format(
                        now.strftime("%Y-%m-%d")
                    )
                )
                try:
                    Nominal = f"{float(Nominal):.3f}"
                except (ValueError, TypeError):
                    Nominal = str(Nominal)

                try:
                    Readings = f"{float(Readings):.3f}"
                except (ValueError, TypeError):
                    Readings = str(Readings)

                try:
                    Correction = f"{float(Correction):.3f}"
                except (ValueError, TypeError):
                    Correction = str(Correction)

                try:
                    Tool_value = f"{float(Tool_value):.3f}"
                except (ValueError, TypeError):
                    Tool_value = str(Tool_value)
                with _csv_lock:

                    os.makedirs(CSV_DIRECTORY, exist_ok=True)

                    needs_header = (
                        not os.path.exists(csv_path)
                        or os.path.getsize(csv_path) == 0
                    )

                    with open(
                        csv_path,
                        "a",
                        newline="",
                        encoding="utf-8"
                    ) as csv_file:

                        writer = csv.writer(csv_file)

                        if needs_header:
                            writer.writerow(CSV_HEADER)

                        writer.writerow([
                            Sr_No,
                            Program_id,
                            Partname,
                            Dimension,
                            Job_count,
                            Machine,
                            Tool_no,
                            Nominal,
                            Readings,
                            Correction,
                            Tool_value,
                            now.strftime("%Y-%m-%d"),
                            now.strftime("%H:%M:%S"),
                        ])

                return csv_path
            except Exception as e:
                print(f"Error in export_to_csv -> {e}")

    def export_filtered_report(self, program_id, from_date, to_date):
        """Export selected program/date-range AOC CSV rows to an Excel workbook."""
        try:
            if from_date > to_date:
                raise ValueError("From date cannot be later than To date.")
            usb_path = self._get_usb_path()
            if usb_path is None:
                raise RuntimeError("USB drive not detected. Insert a USB drive and try again.")

            rows_by_dimension = {}
            for filename in os.listdir(CSV_DIRECTORY) if os.path.isdir(CSV_DIRECTORY) else []:
                if not (filename.startswith("aoc_corrections_") and filename.endswith(".csv")):
                    continue
                file_date_text = filename[len("aoc_corrections_"):-len(".csv")]
                try:
                    file_date = datetime.strptime(file_date_text, "%Y-%m-%d").date()
                except ValueError:
                    continue
                if not from_date <= file_date <= to_date:
                    continue

                csv_path = os.path.join(CSV_DIRECTORY, filename)
                with open(csv_path, newline="", encoding="utf-8") as csv_file:
                    for row in csv.DictReader(csv_file):
                        if str(row.get("Program_id", "")).strip() != str(program_id).strip():
                            continue
                        dimension = (row.get("Dimension") or "Unknown").strip() or "Unknown"
                        rows_by_dimension.setdefault(dimension, []).append(row)

            if not rows_by_dimension:
                return None, 0

            export_directory = os.path.join(usb_path, "Octo_Csv")
            os.makedirs(export_directory, exist_ok=True)
            filename = "Report_{}_{}_to_{}.xlsx".format(
                program_id,
                from_date.strftime("%Y-%m-%d"), 
                to_date.strftime("%Y-%m-%d")
            )
            output_path = os.path.join(export_directory, filename)
            total_rows = sum(len(rows) for rows in rows_by_dimension.values())
            self.write_xlsx(output_path, rows_by_dimension)
            return output_path, total_rows
        except Exception as e:
            print(f"Error in export_filtered_report -> {e}")

    @staticmethod
    def _get_usb_path():
        """Return the currently mounted USB storage path.

        Works even when USB is inserted after the application has started.
        Ignores stale directories left under /media.
        """

        try:
            media_stat = os.stat(USB_MOUNT_DIRECTORY)
            media_device = media_stat.st_dev

            for name in os.listdir(USB_MOUNT_DIRECTORY):

                mount_point = os.path.join(
                    USB_MOUNT_DIRECTORY,
                    name
                )

                # Must be a directory
                if not os.path.isdir(mount_point):
                    continue

                try:
                    usb_stat = os.stat(mount_point)

                    # IMPORTANT:
                    # If st_dev is the same as /media,
                    # this is only a normal directory, not a mounted USB.
                    if usb_stat.st_dev == media_device:
                        print(
                            f"[USB] Ignoring stale/non-mounted directory: "
                            f"{mount_point}"
                        )
                        continue

                    # Check writable
                    if not os.access(mount_point, os.W_OK):
                        print(
                            f"[USB] USB found but not writable: "
                            f"{mount_point}"
                        )
                        continue

                    print(
                        f"[USB] Current USB detected: "
                        f"{mount_point}"
                    )

                    return mount_point

                except OSError as e:
                    print(
                        f"[USB] Cannot inspect {mount_point}: {e}"
                    )
                    continue

        except OSError as e:
            print(
                f"[USB] Cannot access {USB_MOUNT_DIRECTORY}: {e}"
            )

        print("[USB] No currently mounted USB found")

        return None
    
    @staticmethod
    def write_xlsx(output_path, rows_by_dimension):
        """
        Create a valid XLSX workbook using Python standard library only.

        One worksheet is created for each dimension.
        """
        try:
            dimensions = sorted(rows_by_dimension)

            def xml_escape(value):
                if value is None:
                    return ""

                return escape(
                    str(value),
                    {'"': '&quot;', "'": '&apos;'}
                )

            def column_name(index):
                name = ""

                while index:
                    index, remainder = divmod(index - 1, 26)
                    name = chr(65 + remainder) + name

                return name

            def make_cell(column, row_number, value):
                """
                Always write CSV values as strings.
                This preserves 20.600 exactly.
                """

                text = xml_escape(value)

                return (
                    '<c r="{column}{row}" t="inlineStr">'
                    '<is><t xml:space="preserve">{text}</t></is>'
                    '</c>'
                ).format(
                    column=column,
                    row=row_number,
                    text=text
                )

            def make_sheet_xml(rows):
                worksheet_rows = []

                # =========================================================
                # HEADER ROW
                # =========================================================
                header_cells = ""

                for index, header in enumerate(
                    CSV_HEADER,
                    start=1
                ):
                    header_cells += make_cell(
                        column_name(index),
                        1,
                        header
                    )

                worksheet_rows.append(
                    '<row r="1">{}</row>'.format(
                        header_cells
                    )
                )

                # =========================================================
                # DATA ROWS
                # Reset Sr.No from 1 for EVERY dimension sheet
                # =========================================================
                for row_number, row_data in enumerate(
                    rows,
                    start=2
                ):

                    cells = ""

                    for index, header in enumerate(
                        CSV_HEADER,
                        start=1
                    ):

                        # -------------------------------------------------
                        # Sr.No:
                        # Excel sheet D1 -> starts 1
                        # Excel sheet D2 -> starts 1
                        # Excel sheet D3 -> starts 1
                        # -------------------------------------------------
                        if header == "Sr.No":
                            value = row_number - 1
                        else:
                            value = row_data.get(
                                header,
                                ""
                            )

                        cells += make_cell(
                            column_name(index),
                            row_number,
                            value
                        )

                    worksheet_rows.append(
                        '<row r="{}">{}</row>'.format(
                            row_number,
                            cells
                        )
                    )

                last_column = column_name(
                    len(CSV_HEADER)
                )

                last_row = len(rows) + 1

                return (
                    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    '<worksheet '
                    'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                    '<dimension ref="A1:{last_column}{last_row}"/>'
                    '<sheetViews>'
                    '<sheetView workbookViewId="0"/>'
                    '</sheetViews>'
                    '<sheetData>{rows}</sheetData>'
                    '</worksheet>'
                ).format(
                    last_column=last_column,
                    last_row=last_row,
                    rows="".join(worksheet_rows)
                )
            # ---------------------------------------------------------
            # WORKBOOK
            # ---------------------------------------------------------

            workbook_sheets = ""

            relationships = ""

            content_types = ""

            for index, dimension in enumerate(
                dimensions,
                start=1
            ):

                safe_name = str(dimension).strip()

                if not safe_name:
                    safe_name = "Unknown"

                # Excel sheet name maximum = 31 characters
                safe_name = safe_name[:31]

                workbook_sheets += (
                    '<sheet name="{name}" '
                    'sheetId="{sheet_id}" '
                    'r:id="rId{rel_id}"/>'
                ).format(
                    name=xml_escape(safe_name),
                    sheet_id=index,
                    rel_id=index
                )

                relationships += (
                    '<Relationship '
                    'Id="rId{index}" '
                    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" '
                    'Target="worksheets/sheet{index}.xml"/>'
                ).format(
                    index=index
                )

                content_types += (
                    '<Override '
                    'PartName="/xl/worksheets/sheet{index}.xml" '
                    'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                ).format(
                    index=index
                )

            workbook_xml = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<workbook '
                'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                '<bookViews>'
                '<workbookView activeTab="0"/>'
                '</bookViews>'
                '<sheets>{}</sheets>'
                '</workbook>'
            ).format(
                workbook_sheets
            )

            workbook_relationships = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships '
                'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship '
                'Id="rId1" '
                'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
                'Target="xl/workbook.xml"/>'
                '</Relationships>'
            )

            worksheet_relationships = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships '
                'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '{}'
                '</Relationships>'
            ).format(
                relationships
            )

            content_types_xml = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Types '
                'xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                '<Default Extension="rels" '
                'ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                '<Default Extension="xml" '
                'ContentType="application/xml"/>'
                '<Override '
                'PartName="/xl/workbook.xml" '
                'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                '{}'
                '</Types>'
            ).format(
                content_types
            )

            # ---------------------------------------------------------
            # WRITE XLSX
            # ---------------------------------------------------------

            with zipfile.ZipFile(
                output_path,
                "w",
                zipfile.ZIP_DEFLATED
            ) as workbook_file:

                # Content types
                workbook_file.writestr(
                    "[Content_Types].xml",
                    content_types_xml
                )

                # Root relationships
                workbook_file.writestr(
                    "_rels/.rels",
                    workbook_relationships
                )

                # Workbook
                workbook_file.writestr(
                    "xl/workbook.xml",
                    workbook_xml
                )

                # Workbook relationships
                workbook_file.writestr(
                    "xl/_rels/workbook.xml.rels",
                    worksheet_relationships
                )

                # Worksheets
                for index, dimension in enumerate(
                    dimensions,
                    start=1
                ):

                    sheet_xml = make_sheet_xml(
                        rows_by_dimension[dimension]
                    )

                    workbook_file.writestr(
                        "xl/worksheets/sheet{}.xml".format(index),
                        sheet_xml
                    )
        except Exception as e:
            print(f"Error in write_xlsx ->{e}")
    