def make_shirt(size, message):
	"""Displays t-shirt size and message"""
	print(f"\nYou requested a {size} t-shirt.")
	print(f"{message.title()} will be printed on your t-shirt.")

# make_shirt('medium', 'Jamaica')
make_shirt(message='USA', size='large')
