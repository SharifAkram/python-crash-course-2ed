# Store information about a pizza being ordered

'''

When you need to break up a long line in a print() call, 
choose an appropriate point at which to break the line being printed, 
and end the line with a quotation mark. Indent the next line, 
add an opening quotation mark, and continue the string. 
Python will automatically combine all of the strings 
it finds inside the parentheses.


pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

	# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza " #
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

'''

def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

'''

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''