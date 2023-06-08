import unittest


from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Does a simple city and country pair work?"""
		miami_united_states = city_country('miami', 'united states')
		self.assertEqual(miami_united_states, 'Miami, United States')

	def test_city_country_population(self):
		"""Can I include a population argument?"""
		miami_united_states = city_country('miami', 'united states', population=6215000 )
		self.assertEqual(miami_united_states, 'Miami, United States - population 6215000')


if __name__ == '__main__':
	unittest.main()