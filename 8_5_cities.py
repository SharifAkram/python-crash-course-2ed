def describe_city(city, country='united states'):
	"""Describe a city and country."""
	message = f"{city.title()} is in {country.title()}.\n"
	print(message)

describe_city('miami')
describe_city(city='astana', country='kazakhstan')
describe_city('atlanta')