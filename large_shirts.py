def make_shirt(size='large', message='I love Python!'):
	"""Displayes t-shirt size and message."""
	print(f"\nI'm going to make a {size} t-shirt.")
	print(f'It will say, "{message.title()}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'humans are crazy!')