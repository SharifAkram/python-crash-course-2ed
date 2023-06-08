class MyCounter:

	def set_count(self, n):
		self.count = n

mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)

class Employee:
	
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    def monthly_salary(self):
    	"""Add monthly_salary method that 
    	returns 1/12th of salary attribute."""
        return self.salary / 12
    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)
