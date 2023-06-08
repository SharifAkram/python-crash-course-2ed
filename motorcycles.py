print("Examples of lists:\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'bmw'
print(motorcycles)

motorcycles[1] = 'harley davidson'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
 
'''
To put users in control of data, start by defining an empty list that will hold the user's value. 
Then append each new value provided to the list you just created. Below is an example. 
'''

print("\nAppend example:\n")

motorcycles = [] 

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("\nInsert elements:\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

print("\nDelete elements:\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

print("\nPop elements:\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"\nThe last motorcycle I owned was a {last_owned.title()}.\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")

print("Remove elements:\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

print("\nRemove example declaring varibale and using f string\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print("\nAvoiding index errors:\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])	# Index -1 always returns the last item in a list


