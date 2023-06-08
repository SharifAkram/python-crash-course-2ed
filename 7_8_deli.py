sandwich_orders = [
	'cheese', 'ham and cheese', 'ham salad', 'sausage', 
	'cheese and onion', 'egg mayonnaise']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I am working on your {current_sandwich} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
	print(f"I made a {sandwich} sandwich.")