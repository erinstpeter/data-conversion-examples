# Read vegetables.csv
# Convert it to dictionaries

import csv
with open('veggies.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)




#Write it to json
import json
with open('veggies.json', 'w') as f:
		json.dump(rows, f)