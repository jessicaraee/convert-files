#Batch convert folder of xls files to xlsx

import os
import pandas as pd

#Configure files
INPUT_FOLDER = 'INPUT FOLDER' #Update to filepath and name
OUTPUT_FOLDER = os.path.join(source_folder, 'Converted') #Update to desired new folder name

def convert_xls_to_xlsx(source_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    xls_files = [f for f in os.listdir(folder_path) if f.endswith('.xls') and not f.startswith('~$')]
    
    if not xls_files:
        print("No .xls files found.")
        return

    for file in xls_files:
        xls_path = os.path.join(source_folder, file)
        xlsx_filename = file.replace('.xls', '.xlsx')
        xlsx_path = os.path.join(output_folder, xlsx_filename)

        try:
            df = pd.read_excel(xls_path, engine='xlrd')
            df.to_excel(xlsx_path, index=False, engine='openpyxl')
            print(f"Converted: {file} → {xlsx_filename}")
        except Exception as e:
            print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":  
    if os.path.isdir(source_folder):
        convert_xls_to_xlsx(source_folder, output_folder)
        print(f"\nConverted files saved in: {output_folder}.")

        os.system(f'open "{output_folder}"')
    else:
        print("Invalid folder path.")
