'''
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")
'''

"""A collection of classes for modeling users."""

class User:
	"""Summarize attributes of a user."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.login_attempts = 0

	def describe_user(self):
		"""Display a summary of the user's information."""
		print(f"\n{self.first_name} {self.last_name}")
		print(f" Username: {self.username}")
		print(f" Email: {self.email}")
		print(f" Location: {self.location}")

	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print(f"\nWelcome back, {self.username}!")

	def incremement_login_attempts(self):
		"""Incremenets the value of login_attempts."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login_attempts to 0."""
		self.login_attempts = 0