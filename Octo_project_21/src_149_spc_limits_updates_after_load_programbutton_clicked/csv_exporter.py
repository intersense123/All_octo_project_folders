#!/usr/bin/env python3
"""
CSV Export class for ProbeBasedIds + ProbeValues combined data from OctoPreciGo.db.
Exports pipe-delimited combined strings to date-wise CSV files.
"""

import sqlite3
import csv
import os
from datetime import datetime
from typing import Optional


class CSVExport:
    def __init__(self, db_path: str = "/home/torizon/app/data/OctoPreciGo.db"):
        self.db_path = db_path

        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database not found: {db_path}")

        # CSV folder
        self.csv_folder = "/home/torizon/app/data/Octo_CSV"

        # Create folder if missing
        os.makedirs(self.csv_folder, exist_ok=True)

    def export_to_csv(self, probe_id: Optional[int] = None):
        """
        Export combined Probe data to a date-wise CSV.

        CSV Name:
            13-07-2026.csv

        Each row contains:
        ProbeUniqueSettings|Id|ProbeBasedId|GlobalCounter|Mode|JobCount|Value|Status
        """

        # Date-wise CSV path
        today = datetime.now().strftime("%d-%m-%Y")
        csv_path = os.path.join(self.csv_folder, f"{today}.csv")

        # Header only if file doesn't exist
        file_exists = os.path.isfile(csv_path)

        where_clause = "WHERE p.ProbeId = ?" if probe_id else ""
        params = [probe_id] if probe_id else []

        query = f"""
        SELECT
            p.ProbeUniqueSettings,
            v.Id,
            v.ProbeBasedId,
            v.GlobalCounter,
            v.Mode,
            v.JobCount,
            v.Value,
            v.Status
        FROM ProbeBasedIds p
        LEFT JOIN ProbeValues v
            ON p.ProbeId = v.ProbeBasedId
        {where_clause}
        ORDER BY COALESCE(v.ProbeBasedId, p.ProbeId),
                 v.GlobalCounter,
                 v.Id
        """

        row_count = 0

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute(query, params)

            # Append if today's file already exists
            with open(csv_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                # Write header only once
                if not file_exists:
                    writer.writerow(["CombinedData"])

                for row in cursor:
                    fields = [
                        row["ProbeUniqueSettings"],
                        str(row["Id"]),
                        str(row["ProbeBasedId"]),
                        str(row["GlobalCounter"]),
                        row["Mode"] or "",
                        str(row["JobCount"]) if row["JobCount"] is not None else "",
                        str(row["Value"]) if row["Value"] is not None else "",
                        row["Status"] or "",
                    ]

                    writer.writerow(["|".join(fields)])
                    row_count += 1

        return row_count, csv_path