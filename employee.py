class Employee:
	"""
	Class to represent an employee, including first name,
	last name, annual salary. 
	"""
	def __init__(self, f_name, l_name, salary):
		"""Initialize the employee."""
		self.first = f_name.title()
		self.last = l_name.title()
		self.salary = salary

	def give_raise(self, amount=5000):
		"""Give the employee a raise."""
		self.salary += amount
