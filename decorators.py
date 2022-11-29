#Python Decorators

class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name !')
        self.first = None
        self.last = None


emp_1 = Employee('Gawsik','Kannan',10000)
emp_2 = Employee('Corey','Rambo',20000)

print(emp_1.first)
print(emp_1.email)

emp_1.first = 'Kumaran'

print(emp_1.first)
print(emp_1.email)

print(emp_1.fullname)

emp_1.fullname = 'Jerry GK'

print(emp_1.fullname) 
print(emp_1.email)

del emp_1.fullname

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)

