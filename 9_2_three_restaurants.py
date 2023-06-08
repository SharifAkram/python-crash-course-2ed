class Restaurant:
	"""A class representing a restaurant."""

	def __init__(self, name, cuisine_type):
		"""Initialize the restaurant."""
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		msg = f"{self.name} serves wonderful {self.cuisine_type}."
		print(f"\n{msg}")

	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		msg = f"{self.name} is open. Come in!"
		print(f"\n{msg}")

bakerist = Restaurant('bakerist', 'greek salad')
bakerist.describe_restaurant()

flashback_diner = Restaurant('flashback diner', 'buffalo wings')
flashback_diner.describe_restaurant()

tandoor = Restaurant('tandoor', 'butter chicken')
tandoor.describe_restaurant()