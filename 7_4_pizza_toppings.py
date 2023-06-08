prompt = "\nPlease enter the pizza toppings you would like?"
prompt += "\nWhen you are finished, please write 'done' \
to terminate the program: "

while True:
	topping = input(prompt)
	if topping != 'done':
		print(f"I'll add {topping} to your pizza.")
	else:
		break