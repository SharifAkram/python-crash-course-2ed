magicians = ['alice', 'david', 'carolina']
for magician in magicians:	# For every magician in the list of magicianss, print the magician's name
	print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
		print(f"\n{magician.title()}, that was a great trick!")	# Indented line follwoing for loop is considered inside the loop
		print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was great magic show!")

