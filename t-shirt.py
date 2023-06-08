def make_shirt(size, message):
	"""Displays t-shirt size and message"""
	print(f"\nYou requested a {size} t-shirt.")
	print(f"{message.title()} will be printed on your t-shirt.")

# make_shirt('medium', 'pro-choice')
make_shirt(message='trump 2024', size='large')