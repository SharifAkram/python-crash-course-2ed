# Import datetime from datetime
from datetime import datetime

class Employee:
	"""Attributes of an employee."""

	def __init__(self, name, salary=0):
		"""Intialize attributes of an employee."""
		self.name = name.title()
		if salary > 0:
			self.salary = salary
		else:
			self.salary = 0
			print("Invalid salary!")

		self.hire_date = datetime.today()

emp = Employee('sharif akram')
print(emp.name)
print(emp.hire_date)