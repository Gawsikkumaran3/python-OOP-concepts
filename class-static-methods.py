#Class static methods
class Employee:

    raise_amount = 1.04
    no_of_employees = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        #self.pay = int(self.pay*1.04)
        #self.pay = int(self.pay*Employee.raise_amount)
        self.pay = int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def isweekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Gawsik','Kannan',10000)
emp_2 = Employee('Corey','Rambo',20000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.set_raise_amount(2))

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)




# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# # Employee.raise_amount = 1.05
# Employee.set_raise_amount(1.06)
# # emp_1.set_raise_amount(1.07)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str = 'Tom-Harry-50000'

# # first , last , pay = emp_str.split('-')
# # emp_new = Employee(first,last,pay)

# emp_new = Employee.from_string(emp_str)
# print(emp_new.email)

# import datetime

# my_date = datetime.date(2022,11,27)
# print(Employee.isweekday(my_date))
