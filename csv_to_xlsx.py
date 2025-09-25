#Convert CSV to XLSX

import pandas as pd

INPUT_FILE = "/FILEPATH/INPUTFILE.csv"
OUTPUT_FILE = "/FILEPATH/OUTPUTFILE.xlsx"

df = pd.read_csv(INPUT_FILE)
df.to_excel(OUTPUT_FILE, index=False)
