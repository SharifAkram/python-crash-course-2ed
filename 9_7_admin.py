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

class Admin(User):
	"""A user with administrative privileges."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, email, location)
		self.privileges = []

	def show_privileges(self):
		"""Display the privileges this administrator has."""
		print("\nPrivileges:")
		for privilege in self.privileges:
			print(f" - {privilege}")

sharif = Admin('sharif', 'akram', 'rifkit', 'rifkit@gmail.com', 'hallandale beach')
sharif.describe_user()

sharif.privileges = [
	'can reset passwords',
	'can moderate discussons',
	'can suspend accounts',
	]

sharif.show_privileges()