dinner_group = input("\nHow many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group >= 8:
	print("\nYou will have to wait for a table.")
else:
	print("\nYour table is ready.")
