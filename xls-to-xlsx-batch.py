#Batch convert folder of xls files to xlsx

import os
import pandas as pd
import csv

#Configure files
INPUT_FOLDER = '/FILEPATH/INPUTFOLDER'
OUTPUT_FOLDER = '/FILEPATH/OUTPUTFOLDER'
OUTPUT_FILE = '/FILEPATH/OUTPUTFILE.xlsx'

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

#Find all .xls files and convert to .xlsx
files = [
    f for f in os.listdir(INPUT_FOLDER)
    if f.lower().endswith(('.xls', '.xlsx')) and not f.startswith('~$')
]

if not files:
    print("No .xls files found.")
else:
    failed_files = []

    for file in files:
        input_path = os.path.join(INPUT_FOLDER, file)
        output_filename = os.path.splitext(file)[0] + '.xlsx'
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        try:
            try:
                df = pd.read_excel(input_path)
            except Exception:
                with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
                    sample = f.read(2048)
                    f.seek(0)
                    dialect = csv.Sniffer().sniff(sample)
                    df = pd.read_csv(f, sep=dialect.delimiter)

            df.to_excel(output_path, index=False, engine='openpyxl')
            print(f"Converted {file} → {output_filename}")

        except Exception as e:
            print(f"Could not convert {file}: {e}")
            failed_files.append((file, str(e)))

    if failed_files:
        print("\nSome files could not be converted:")
        for f, err in failed_files:
            print(f"- {f}: {err}")

    print(f"\nConverted files saved in {OUTPUT_FOLDER}")
    os.system(f'open "{OUTPUT_FOLDER}"')

#Export a list counting the rows in each file created above to verify files converted correctly
row_counts = []

for filename in os.listdir(OUTPUT_FOLDER):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(OUTPUT_FOLDER, filename)
        try:
            df = pd.read_excel(filepath, engine='openpyxl')

            data_rows = df.shape[0]
            row_counts.append({"File Name": filename, "Row Count": data_rows})

        except Exception as e:
            row_counts.append({"File Name": filename, "Row Count": f"ERROR: {e}"})

summary_df = pd.DataFrame(row_counts)
summary_df.to_excel(OUTPUT_FILE, index=False)
print(f"Row counts saved to {OUTPUT_FILE}")
print(summary_df)
