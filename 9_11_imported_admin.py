from user import Admin

sharif = Admin('sharif', 'akram', 'rifkit', 'rifkit@gmail.com', 'florida')
sharif.describe_user()

sharif_privileges = [
	'can reset passwords',
	'can moderate discussions',
	'can suspend accounts',
	]

sharif.privileges.privileges = sharif_privileges

print(f"\nThe admin {sharif.username} has these privileges: ")
sharif.privileges.show_privileges()