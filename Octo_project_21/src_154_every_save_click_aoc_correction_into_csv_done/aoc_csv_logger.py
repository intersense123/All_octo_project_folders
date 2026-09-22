"""Append AOC correction cycles to date-wise CSV files."""

import csv
import os
from datetime import datetime
from threading import Lock


CSV_DIRECTORY = "/home/torizon/app/data/Octo_CSV"
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
