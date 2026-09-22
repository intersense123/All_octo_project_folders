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
    "Machine",
    "Dimension",
    "Partname",
    "Nominal",
    "Readings",
    "Correction",
    "Tool_value",
    "Tool_no",
    "Job count",
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
            Machine,
            Dimension,
            Partname,
            Nominal,
            Readings,
            Correction,
            Tool_value,
            Tool_no,
            Job_count,
        ):
            """
            Save one AOC correction cycle to the daily CSV file.

            CSV format:
            Sr.No, Program_id, Machine, dimension, partname, nominal,
            reading, correction, tool_value, tool_no, job count, date, time
            """

            now = datetime.now()

            csv_path = os.path.join(
                CSV_DIRECTORY,
                "aoc_corrections_{}.csv".format(
                    now.strftime("%Y-%m-%d")
                )
            )
            try:
                nominal = f"{float(Nominal):.3f}"
            except (ValueError, TypeError):
                nominal = str(Nominal)

            try:
                reading = f"{float(Readings):.3f}"
            except (ValueError, TypeError):
                reading = str(Readings)

            try:
                correction = f"{float(Correction):.3f}"
            except (ValueError, TypeError):
                correction = str(Correction)

            try:
                tool_value = f"{float(Tool_value):.3f}"
            except (ValueError, TypeError):
                tool_value = str(Tool_value)
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
                        Machine,
                        Dimension,
                        Partname,
                        Nominal,
                        Readings,
                        Correction,
                        Tool_value,
                        Tool_no,
                        Job_count,
                        now.strftime("%Y-%m-%d"),
                        now.strftime("%H:%M:%S"),
                    ])

            return csv_path

    def export_filtered_report(self, program_id, from_date, to_date):
        """Export selected program/date-range AOC CSV rows to an Excel workbook."""
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
        filename = "Report_{}_to_{}.xlsx".format(
            from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d")
        )
        output_path = os.path.join(export_directory, filename)
        total_rows = sum(len(rows) for rows in rows_by_dimension.values())
        self._write_xlsx(output_path, rows_by_dimension)
        return output_path, total_rows

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
    def _write_xlsx(output_path, rows_by_dimension):
        """
        Create a valid XLSX workbook using Python standard library only.

        One worksheet is created for each dimension.
        """

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

            # Header
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

            # Data
            for row_number, row_data in enumerate(
                rows,
                start=2
            ):

                cells = ""

                for index, header in enumerate(
                    CSV_HEADER,
                    start=1
                ):

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
    # def _write_xlsx(output_path, rows_by_dimension):
    #     """Write a minimal standards-compliant XLSX workbook using stdlib only."""
    #     dimensions = sorted(rows_by_dimension)

    #     def cell(column, row, value):
    #         text = escape(str(value if value is not None else ""))
    #         return '<c r="{}{}" t="inlineStr"><is><t>{}</t></is></c>'.format(column, row, text)

    #     def column_name(index):
    #         name = ""
    #         while index:
    #             index, remainder = divmod(index - 1, 26)
    #             name = chr(65 + remainder) + name
    #         return name

    #     def sheet_xml(rows):
    #         worksheet_rows = []
    #         all_rows = [CSV_HEADER] + [[row.get(name, "") for name in CSV_HEADER] for row in rows]
    #         for row_number, values in enumerate(all_rows, 1):
    #             cells = "".join(cell(column_name(index), row_number, value)
    #                             for index, value in enumerate(values, 1))
    #             worksheet_rows.append('<row r="{}">{}</row>'.format(row_number, cells))
    #         return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    #                 '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
    #                 '<sheetData>{}</sheetData></worksheet>').format("".join(worksheet_rows))

    #     sheets = "".join(
    #         '<sheet name="{}" sheetId="{}" r:id="rId{}"/>'.format(escape(name[:31]), index, index)
    #         for index, name in enumerate(dimensions, 1)
    #     )
    #     workbook = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    #                 '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
    #                 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
    #                 '<sheets>{}</sheets></workbook>').format(sheets)
    #     relationships = ''.join(
    #         '<Relationship Id="rId{}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{}.xml"/>'.format(index, index)
    #         for index in range(1, len(dimensions) + 1)
    #     )
    #     content_types = ''.join(
    #         '<Override PartName="/xl/worksheets/sheet{}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'.format(index)
    #         for index in range(1, len(dimensions) + 1)
    #     )

    #     with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as workbook_file:
    #         workbook_file.writestr("[Content_Types].xml", ('<?xml version="1.0" encoding="UTF-8"?>'
    #             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    #             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    #             '<Default Extension="xml" ContentType="application/xml"/>'
    #             '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
    #             '{}</Types>').format(content_types))
    #         workbook_file.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
    #         workbook_file.writestr("xl/workbook.xml", workbook)
    #         workbook_file.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{}</Relationships>'.format(relationships))
    #         for index, dimension in enumerate(dimensions, 1):
    #             workbook_file.writestr("xl/worksheets/sheet{}.xml".format(index), sheet_xml(rows_by_dimension[dimension]))
