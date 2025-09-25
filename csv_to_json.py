#Convert CSV to JSON

import csv
import json
from collections import defaultdict

INPUT_FILE = "/FILEPATH/INPUTFILE.csv"
OUTPUT_FILE = "/FILEPATH/OUTPUTFILE.json"

with open(INPUT_FILE, 'r', newline='', encoding='utf-8') as csvfile, open(OUTPUT_FILE, 'w', encoding='utf-8') as jsonfile:

    reader = csv.DictReader(csvfile)

    output_fields = {"field_1", "field_2", "field_3", "field_4", "field_5"}

    all_records = []
    for row in reader:
        filtered = {k: v for k, v in row.items() if k in output_fields}
        all_records.append(filtered)

    json.dump(all_records, jsonfile, indent=2)
