"""A collection of funcations for working with cities."""


''' Failed
def city_country(city, country, population):
	"""Return a string like 'City, Country - population'."""
	output_string = f"{city.title()}, {country.title()}"
	output_string += f" - population {populaion}"
	return output_string
'''

def city_country(city, country, population=''):
	"""Return a tring representing a city-country pair."""

	output_string = f"{city.title()}, {country.title()}"
	if population:
		output_string += f" - population {population}"
	return output_string