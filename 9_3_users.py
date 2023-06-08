class User:
	"""Summarize attributes of a user."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()

	def describe_user(self):
		"""Display a summary of the user's information."""
		print(f"\n{self.first_name} {self.last_name}")
		print(f" Username: {self.username}")
		print(f" Email: {self.email}")
		print(f" Location: {self.location}")

	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"\nWelcome back, {self.username}!")

sharif = User('sharif', 'akram', 'rifkit', 'rifkit@gmail.com', 'hallandale beach')
sharif.describe_user()
sharif.greet_user()

debra = User('debra', 'carter', 'dcdeerfield', 'dcdeerfield@gmail.com', 'coconut creek')
debra.describe_user()
debra.greet_user()

cyrano = User('cyrano', 'irons', 'histori', 'historimastermind@gmail.com', 'nashville')
cyrano.describe_user()
cyrano.greet_user()

