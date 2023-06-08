def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('sharif', 'akram', 
							   location='hallandale beach', 
							   field='international business development',
							   age=37, marriage_status='single', children=1,
							   highest_degree='masters',
							   )

print(user_profile)