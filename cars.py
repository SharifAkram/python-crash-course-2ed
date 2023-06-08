'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Permanent 
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)	# Reverse true argument puts list in reverse alphabetical order
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list:")
print(cars)

print("\nReverse example:\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()	# Reverses the order of the list, not alphabetically
print(cars)

cars.reverse()	# Apply reverse again to obtain the original order
print(cars)

print("\nFinding the length of a list:\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

'''

def make_car(manufacturer, model, **options):
	"""Make a dictionary representing a car."""
	car_dict = {
		'manufacturer': manufacturer.title(),
		'model': model.title()
		}
	for option, value in options.items():
		car_dict[option] = value 

	return car_dict

my_outback = make_car('suburu', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_corolla = make_car('toyota', 'corolla', year='2011', color='gold', 
						   bought='used', sold='2016'
						  )
print(my_old_corolla)
