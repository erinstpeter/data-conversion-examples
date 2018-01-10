# read superheroes.json

import json
from pprint import pprint

with open('superheroes.json') as f:
	data = json.load(f)

# create a blank list of powers

powers = []

# loop over members

members = data['members']

# for each member, loop over the powers

for member in members:
	member_powers = member ['powers']

	for power in member_powers: 
		# add that to our list of powers
		powers.append(power)

# get only unique powers in list
unique_powers = list(set(powers))

# print 
pprint(unique_powers)
