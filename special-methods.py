#Special methods(super methods)

class Employee:

    raise_amount = 1.04
    
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

    def __repr__(self):
        return "Employee({},{},{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)

    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self): # magic method
        return len(self.fullname())


emp_1 = Employee('Gawsik','Kannan',10000)
emp_2 = Employee('Corey','Rambo',20000)

print(emp_1) #withour repr and str functions
print(emp_1) #without str function
print(emp_1) #with both str and repr functions

print(emp_1.__repr__())
print(emp_1.__str__())

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(Employee.__add__(emp_1,emp_2))
print(emp_1 + emp_2)

print(len(emp_1))
print(Employee.__len__(emp_1))