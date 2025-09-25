#Convert TSV file to XLSX

import csv
from xlsxwriter.workbook import Workbook

INPUT_FILE = "/FILEPATH/INPUTFILE.tsv"
OUTPUT_FILE = "/FILEPATH/OUTPUTFILE.xlsx"

workbook = Workbook(OUTPUT_FILE)
worksheet = workbook.add_worksheet()

read_tsv = csv.reader(open(INPUT_FILE, 'r', encoding='utf-8'), delimiter='\t')

for row, data in enumerate(read_tsv):
    worksheet.write_row(row, 0, data)

workbook.close()
