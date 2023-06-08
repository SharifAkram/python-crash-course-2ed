import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
	"""Test for the module employee."""

	def setUp(self):
		"""Make and employee to use in tests."""
		self.sharif = Employee('sharif', 'akram', 45_000)

	def test_give_default_raise(self):
		"""Test that a default raise works correctly."""
		self.sharif.give_raise()
		self.assertEqual(self.sharif.salary, 50000)

	def test_give_custom_raise(self):
		"""Test that a custom raise works correctly."""
		self.sharif.give_raise(25000)
		self.assertEqual(self.sharif.salary, 70000)


if __name__ == '__main__':
	unittest.main()
