#Convert JSON file to XLSX

import pandas as pd

INPUT_FILE = '/FILEPATH/INPUTFILE.json'
OUTPUT_FILE = '/FILEPATH/OUTPUTFILE.xlsx'

df = pd.read_json(INPUT_FILE)
df.to_excel(OUTPUT_FILE,index=False)
