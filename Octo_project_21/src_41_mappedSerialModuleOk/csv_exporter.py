#!/usr/bin/env python3
"""
CSV Export class for ProbeBasedIds + ProbeValues combined data from OctoPreciGo.db.
Exports pipe-delimited combined strings to CSV (handles ~10000 rows).
"""

import sqlite3
import csv
import os
from pathlib import Path
from typing import Optional

class CSVExport:
    def __init__(self, db_path: str = "/home/torizon/app/octo.db"):
        self.db_path = db_path
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database not found: {db_path}")

    def export_to_csv(self, csv_path: str = "/home/torizon/app/probe_data.csv", probe_id: Optional[int] = None):
        """
        Export combined Probe data to CSV.
        Each row: ProbeUniqueSettings|Id|ProbeBasedId|GlobalCounter|Mode|JobCount|Value|Status (pipe-delimited in 'CombinedData' column).
        
        Args:
            csv_path: Output CSV path.
            probe_id: Optional filter to specific ProbeId.
        """
        where_clause = "WHERE p.ProbeId = ?" if probe_id else ""
        params = [probe_id] if probe_id else []

        query = """
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
        LEFT JOIN ProbeValues v ON p.ProbeId = v.ProbeBasedId
        """ + where_clause + """
        ORDER BY COALESCE(v.ProbeBasedId, p.ProbeId), v.GlobalCounter, v.Id
        """

        row_count = 0
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row  # Dict-like rows
            cursor = conn.execute(query, params)
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['CombinedData'])  # Header: single column for pipe-string
                
                for row in cursor:
                    # Combine: ProbeUniqueSettings + | + other fields as str
                    fields = [
                        row['ProbeUniqueSettings'],
                        str(row['Id']),
                        str(row['ProbeBasedId']),
                        str(row['GlobalCounter']),
                        row['Mode'],
                        str(row['JobCount']) if row['JobCount'] is not None else '',
                        str(row['Value']) if row['Value'] is not None else '',
                        row['Status'] or ''
                    ]
                    combined = '|'.join(fields)
                    writer.writerow([combined])
                    row_count += 1

        print(f"Exported {row_count} rows to {csv_path}")
        return row_count, csv_path

# if __name__ == "__main__":
#     exporter = CSVExport()
#     exporter.export_to_csv("probe_data.csv")  # Exports all (~10000 rows)
#     # Example: exporter.export_to_csv("probe_1_data.csv", probe_id=1)
# def write_to_csv(data):
# #     data = ['1','2','3']
#     today_date = datetime.now().strftime('%d-%m-%Y')
#     file_path = '/home/pi/Desktop/PreciGo' + '/CSV Files/'+today_date+'.csv'
    
# #     print(file_path)
    
#     # Add "SrNo" as the first column
#     column_names_with_srno = ['Parameter','Guage','Machine','Part_Name','Nominal_Value','Reading','Correction','Tool_Value','Date','Tol_Plus']
    
#     # Check if the file exists
#     file_exists = os.path.isfile(file_path)
    
#     if not file_exists:
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
#     # Open the file in append mode if it exists; otherwise, write mode to create it
#     with open(file_path, mode='a', newline='') as file:
#         writer = csv.writer(file)
        
#         # Write header if file does not exist
#         if not file_exists:
#             # Ensure the directory exists
            
#             writer.writerow(column_names_with_srno)
        
#         # Write data rows with sequential "SrNo"
# #         for index, row in enumerate(data, start=1):
#         writer.writerow(data)
#         file.close()
        
# data = [i.Dimension_Number,Gauge_id,Machine_id,self.current_part_name,
#         mean,float(offs),0,z,
#         str(today.strftime('%d-%m-%Y')),Tool_Number]
                                        
# write_to_csv(data)