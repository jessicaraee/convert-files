#Batch convert folder of xls files to xlsx

import os
import pandas as pd

#Configure files
INPUT_FOLDER = "/filepath/input_folder" #Update with filepath and name 
OUTPUT_FILE = "/filepath/output_file.xlsx" #Update with desired filepath and name

def convert_xls_to_xlsx(INPUT_FOLDER, OUTPUT_FOLDER):
    #Create output folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # List all .xls files in the directory
    xls_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith('.xls') and not f.startswith('~$')]
    
    if not xls_files:
        print("No .xls files found.")
        return

    for file in xls_files:
        xls_path = os.path.join(INPUT_FOLDER, file)
        xlsx_filename = file.replace('.xls', '.xlsx')
        xlsx_path = os.path.join(OUTPUT_FOLDER, xlsx_filename)

        try:
            # Read and convert
            df = pd.read_excel(xls_path, engine='xlrd')
            df.to_excel(xlsx_path, index=False, engine='openpyxl')
            print(f"Converted: {file} → {xlsx_filename}")
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":  
    if os.path.isdir(INPUT_FOLDER):
        convert_xls_to_xlsx(SOURCE_FOLDER, OUTPUT_FOLDER)
        print(f"\nConverted files saved in: {OUTPUT_FOLDER}.")

        #Open the output folder
        os.system(f'open "{OUTPUT_FOLDER}"')
    else:
        print("Invalid folder path.")
