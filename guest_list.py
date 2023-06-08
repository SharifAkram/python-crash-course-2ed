guest_list = ['Heidi', 'Laurel', 'Bilal']
print(guest_list)

will_not_attend = 'Laurel'
print(f"\n{will_not_attend.title()} will not attend the dinner this evening.\n")

guest_list.remove('Laurel')
guest_list.insert(1, 'Rhonda')
print(guest_list)

guest_list.insert(0, 'Dain')
guest_list.insert(3, 'Amira')
guest_list.append('Julian')
print(guest_list)

print("\nI can only invite two people to dinner.")

will_not_attend = guest_list.pop()
print(f"\n{will_not_attend.title()} will not attend this evening.\n")
print(guest_list)

will_not_attend = guest_list.pop()
print(f"\n{will_not_attend.title()} will not attend this evening.\n")
print(guest_list)

will_not_attend = guest_list.pop()
print(f"\n{will_not_attend.title()} will not attend this evening.\n")
print(guest_list)

will_not_attend = guest_list.pop()
print(f"\n{will_not_attend.title()} will not attend this evening.\n")
print(guest_list)

print("\nDain and Heidi are still invited this evening.\n")

del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)

print("\nNo one is invited.\n")