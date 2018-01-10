vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "kale"},
 {"name": "squash"},
 {"name": "broccoli"},
]

print(vegetables)

import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])
	for veggie in vegetables:
		#I want the name of the vegetable
		vegetable_name = veggie['name']
		#I want the length of that word
		vegetable_name_length = len(veggie['name'])
		#Write those to CSV
		writer.writerow([vegetable_name, vegetable_name_length])