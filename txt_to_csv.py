#Convert tab-separated TXT file to CSV

import pandas as pd

INPUT_FILE = "/FILEPATH/INPUTFILE.txt"
OUTPUT_FILE = "/FILEPATH/OUTPUTFILE.csv"

df = pd.read_csv(INPUT_FILE,header=None,sep='\t') #Remove header=None if header is present
df.to_csv(OUTPUT_FILE,index=False)
