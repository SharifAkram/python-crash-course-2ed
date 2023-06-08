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
		
		# Initialize an empty set of privieges.
		self.privileges = Privileges()

class Privileges():
	"""A class to store an admin's privileges."""

	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		print("\nPrivileges:")
		if self.privileges:
			for privilege in self.privileges:
				print(f" - {privilege}")
		else:
			print("- This user has no privileges.")

sharif = Admin('sharif', 'akram', 'rifkit', 'rifkit@gmail.com', 'hallandale beach')
sharif.describe_user()

sharif.privileges.show_privileges()

print("\nAdding privileges...")
sharif_privileges = [
	'can reset passwords',
	'can moderate discussons',
	'can suspend accounts',
	]
sharif.privileges.privileges = sharif_privileges
sharif.privileges.show_privileges()