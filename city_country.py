def city_country(city, country):
	"""Return a string like Miami, United States"""
	return f"{city.title()}, {country.title()}"

city = city_country('miami','united states')
print(city)

city = city_country('atyrau','kazakhstan')
print(city)

city = city_country('lahore','pakistan')
print(city)
