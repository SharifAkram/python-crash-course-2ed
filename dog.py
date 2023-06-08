class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name.title()
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in repsonse to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate solling over in response to a command."""
		print(f"{self.name} rolled over!")


'''
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

'''

my_dog = Dog('romeo', 11)
your_dog = Dog('brownie', 7)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
