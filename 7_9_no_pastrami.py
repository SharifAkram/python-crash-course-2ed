sandwich_orders = [
	'cheese', 'pastrami', 'ham and cheese', 'ham salad', 'sausage', 
	'cheese and onion', 'egg mayonnaise', 'pastrami', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I am working on your {current_sandwich} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
	print(f"I made a {sandwich} sandwich.")