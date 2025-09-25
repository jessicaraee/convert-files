#Combine files stored in a folder into a single file, adding a column naming the original file name as the source file.

import pandas as pd
import os

#Configure files
INPUT_FOLDER = "/FILEPATH/INPUTFOLDER"
OUTPUT_FILE = "/FILEPATH/OUTPUTFILE.xlsx"
LOG_FILE = "/log_report.txt"
FILENAME_SLICE = slice(0, 25) #Change if needed to extract part of filename

#Process files
all_dataframes = []
log_lines = []

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(INPUT_FOLDER, filename)
        try:
            df = pd.read_excel(filepath, engine='openpyxl')

            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            if df.empty or df.dropna(how='all').empty:
                log_lines.append(f"Skipped (empty or all-NA): {filename}")
                continue

            identifier = filename[FILENAME_SLICE].replace(".xlsx", "")
            df['Source.Name'] = identifier

            all_dataframes.append(df)

        except Exception as e:
            log_lines.append(f"ERROR ({filename}): {e}")

#Combine files and export
if all_dataframes:
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    cols = ['Source.Name'] + [col for col in combined_df.columns if col != 'Source.Name']
    combined_df = combined_df[cols]
    combined_df.to_excel(OUTPUT_FILE, index=False)
    print(f"Combined file saved to {OUTPUT_FILE}")
else:
    print("No valid files to process.")

#Write issues log
if log_lines:
    with open(LOG_FILE, "w") as log:
        log.write("Log report for file issues\n")
        log.write("=" * 40 + "\n")
        log.write("\n".join(log_lines))
    print(f"Log report saved to {LOG_FILE}")
else:
    print("No issues to log.")
