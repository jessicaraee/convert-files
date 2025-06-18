#Count rows of data in every file in folder

import pandas as pd
import os

#Configure files
INPUT_FOLDER = "/filepath/input_folder" #Update with filepath and name 
OUTPUT_FILE = "/filepath/output_file.xlsx" #Update with desired filepath and name

row_counts = []

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(INPUT_FOLDER, filename)
        try:
            df = pd.read_excel(filepath, engine='openpyxl')

            # Count rows excluding the header
            data_rows = df.shape[0]  # Number of rows (header not counted in shape)
            row_counts.append({"Filename": filename, "RowCount": data_rows})

        except Exception as e:
            row_counts.append({"Filename": filename, "RowCount": f"ERROR: {e}"})

summary_df = pd.DataFrame(row_counts)
summary_df.to_excel(OUTPUT_FILE, index=False)

print(f"Row counts saved to: {OUTPUT_FILE}")
