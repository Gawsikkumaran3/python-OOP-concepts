#Class variables

class Employee:

    raise_amount = 1.04
    no_of_employees = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = self.first + "." + self.last + "@company.com"
        self.pay = pay

        Employee.no_of_employees = Employee.no_of_employees + 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        #self.pay = int(self.pay*1.04)
        #self.pay = int(self.pay*Employee.raise_amount)
        self.pay = int(self.pay*self.raise_amount)

print(Employee.no_of_employees)

emp_1 = Employee('Gawsik','Kannan',10000)
emp_2 = Employee('Corey','Rambo',20000)

print(Employee.no_of_employees)

# print(Employee.__dict__)
# print(emp_1.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
emp_1.raise_amount=1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)




