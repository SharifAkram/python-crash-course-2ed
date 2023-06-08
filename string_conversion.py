# when to use __repr__ vs __str__

"""
class Car:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def __str__(self):	# dunder str
		return 'a {self.color} car'.format(self = self)

my_car = Car('red', 37281)
print(my_car)

"""

class Car:
	def __init__(self, color, mileage):
		self.color = color
		self.mileage = mileage

	def ___repr__(self):
		return '__repr__ for Car'

	def ___str__(self):
		return '__str__ for Car'

my_car = Car('red', 37281)
print(my_car)