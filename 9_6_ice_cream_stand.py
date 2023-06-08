class Restaurant:
	"""A class representing a restaurant."""

	def __init__(self, name, cuisine_type):
		"""Initialize the restaurant."""
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		msg = f"{self.name} serves wonderful {self.cuisine_type}."
		print(f"{msg}")

	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		msg = f"{self.name} is open. Come in!"
		print(f"\n{msg}")

	def set_number_served(self, number_served):
		"""Allow user to set the number of customers that have been served."""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served

class IceCreamStand(Restaurant):
	"""A class representing an ice cream stand."""

	def __init__(self, name, cuisine_type='ice_cream'):
		"""Initialize an ice cream stand."""
		super().__init__(name, cuisine_type)
		self.flavors = []

	def show_flavors(self):
		"""Display the flavors available."""
		print("\nWe have the following flavors available:")
		for flavor in self.flavors:
			print(f" - {flavor.title()}")

jacksons = IceCreamStand('jacksons')
jacksons.flavors = ['vanilla', 'chocolate', 'chocolate chip cookie dough']

jacksons.describe_restaurant()
jacksons.show_flavors()