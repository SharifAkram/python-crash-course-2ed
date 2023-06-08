rivers = {
	'nile': 'egypt',
	'mississippi': 'united states',
	'fraser': 'canada',
	'missouri': 'united states',
	'yangtze': 'china',
	}

for river, country in rivers.items():
	print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
	print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in set(rivers.values()): # removes duplicate data
	print(f"- {country.title()}")
