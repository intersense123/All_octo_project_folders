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
    "program_id",
    "aoc_id",
    "machine_name",
    "dimension",
    "part_name",
    "mean",
    "offset_no",
    "offs",
    "correction",
    "z",
    "date_time",
]
_csv_lock = Lock()

class AOCExport:
    """Writes AOC correction records to the daily CSV file."""

    def export_to_csv(
        self, program_id, aoc_id, machine_name, dimension, part_name, mean,
        offset_no, offs, correction, z,
    ):
        """Store one AOC reading/correction cycle and return its CSV path.

        A new file is created each day.  The lock keeps a header and row from
        being interleaved when multiple AOC worker jobs finish together.
        """
        now = datetime.now()
        csv_path = os.path.join(
            CSV_DIRECTORY, "aoc_corrections_{}.csv".format(now.strftime("%Y-%m-%d"))
        )

        with _csv_lock:
            os.makedirs(CSV_DIRECTORY, exist_ok=True)
            needs_header = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0
            with open(csv_path, "a", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                if needs_header:
                    writer.writerow(CSV_HEADER)
                writer.writerow([
                    program_id, aoc_id, machine_name, dimension, part_name, mean,
                    offset_no, offs, correction, z,
                    now.strftime("%Y-%m-%d %H:%M:%S"),
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
                    if str(row.get("program_id", "")).strip() != str(program_id).strip():
                        continue
                    dimension = (row.get("dimension") or "Unknown").strip() or "Unknown"
                    rows_by_dimension.setdefault(dimension, []).append(row)

        if not rows_by_dimension:
            return None, 0

        export_directory = os.path.join(usb_path, "Octo_Csv")
        os.makedirs(export_directory, exist_ok=True)
        filename = "AOC_Report_{}_{}_to_{}.xlsx".format(
            program_id, from_date.strftime("%Y-%m-%d"), to_date.strftime("%Y-%m-%d")
        )
        output_path = os.path.join(export_directory, filename)
        total_rows = sum(len(rows) for rows in rows_by_dimension.values())
        self._write_xlsx(output_path, rows_by_dimension)
        return output_path, total_rows

    @staticmethod
    def _get_usb_path():
        """Return the first USB mount path using the updater's /media layout."""
        try:
            for item in sorted(os.listdir(USB_MOUNT_DIRECTORY)):
                usb_path = os.path.join(USB_MOUNT_DIRECTORY, item)
                if os.path.isdir(usb_path):
                    return usb_path
        except OSError:
            pass
        return None

    @staticmethod
    def _write_xlsx(output_path, rows_by_dimension):
        """Write a minimal standards-compliant XLSX workbook using stdlib only."""
        dimensions = sorted(rows_by_dimension)

        def cell(column, row, value):
            text = escape(str(value if value is not None else ""))
            return '<c r="{}{}" t="inlineStr"><is><t>{}</t></is></c>'.format(column, row, text)

        def column_name(index):
            name = ""
            while index:
                index, remainder = divmod(index - 1, 26)
                name = chr(65 + remainder) + name
            return name

        def sheet_xml(rows):
            worksheet_rows = []
            all_rows = [CSV_HEADER] + [[row.get(name, "") for name in CSV_HEADER] for row in rows]
            for row_number, values in enumerate(all_rows, 1):
                cells = "".join(cell(column_name(index), row_number, value)
                                for index, value in enumerate(values, 1))
                worksheet_rows.append('<row r="{}">{}</row>'.format(row_number, cells))
            return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                    '<sheetData>{}</sheetData></worksheet>').format("".join(worksheet_rows))

        sheets = "".join(
            '<sheet name="{}" sheetId="{}" r:id="rId{}"/>'.format(escape(name[:31]), index, index)
            for index, name in enumerate(dimensions, 1)
        )
        workbook = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                    '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                    '<sheets>{}</sheets></workbook>').format(sheets)
        relationships = ''.join(
            '<Relationship Id="rId{}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{}.xml"/>'.format(index, index)
            for index in range(1, len(dimensions) + 1)
        )
        content_types = ''.join(
            '<Override PartName="/xl/worksheets/sheet{}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'.format(index)
            for index in range(1, len(dimensions) + 1)
        )

        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as workbook_file:
            workbook_file.writestr("[Content_Types].xml", ('<?xml version="1.0" encoding="UTF-8"?>'
                '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                '<Default Extension="xml" ContentType="application/xml"/>'
                '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                '{}</Types>').format(content_types))
            workbook_file.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
            workbook_file.writestr("xl/workbook.xml", workbook)
            workbook_file.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{}</Relationships>'.format(relationships))
            for index, dimension in enumerate(dimensions, 1):
                workbook_file.writestr("xl/worksheets/sheet{}.xml".format(index), sheet_xml(rows_by_dimension[dimension]))
