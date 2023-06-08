prompt = "What is your age?\n"
prompt += "\nEnter 'q' to quit. "

while True:
	age = input(prompt)
	if age == 'q':
		break
	age = int(age)

	if age < 3:
		print("\nYour movie ticket is free.")
	elif age < 13:
		print("\nYour movie ticket is $10.")
	else:
		print("\nYour ticket is $15.")