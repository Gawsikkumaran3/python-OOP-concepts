#Python Object Oriented Programming
#Classes and instances

class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

# emp_1 = Employee()
# emp_2 = Employee()

emp_1 = Employee("Gawsik","Kannan",10000)
emp_2 = Employee("Corey","Rambo",20000)

print(emp_1)
print(emp_2)

# emp_1.first = "Gawsik"
# emp_1.last = "Kannan"
# emp_1.email = "Gawsik.kannan@company.com"
# emp_1.pay = 10000

# emp_2.first = "Corey"
# emp_2.last = "Rambo"
# emp_2.email = "Corey.rambo@company.com"
# emp_2.pay = 20000

print(emp_1.email)
print(emp_2.email)

print(emp_1.first+" "+emp_1.last)
print(emp_2.first+" "+emp_2.last)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))