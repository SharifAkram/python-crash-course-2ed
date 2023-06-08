def make_sandwich(*items):
	"""Summarize the items on a sandwich."""
	print(f"Make a sandwich with the following items:")
	for item in items:
		print(f"...adding {item.title()} to your sandwich.")
	print(f"Your sandwich is ready!\n")

make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('cheese', 'bacon')
make_sandwich('beef patty', 'bacon', 'cheese')