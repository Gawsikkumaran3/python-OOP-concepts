#Inheritance

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

class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())



emp_1 = Employee('Gawsik','Kannan',10000)
emp_2 = Employee('Corey','Rambo',20000)

dev_1 = Developer('Tom','Mahe',50000,'Python')
dev_2 = Developer('Jerry','Elan',70000,'Java')

# print(dev_1.fullname())
# print(dev_2.fullname())

# print(help(Developer))

# print(emp_1.pay)
# print(dev_1.pay)

# emp_1.apply_raise()
# dev_1.apply_raise()

# print(emp_1.pay)
# print(dev_1.pay)

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

mgr1 = Manager('Navi','Rohit',80000,[dev_1])

print(mgr1.email)
mgr1.print_emps()
mgr1.add_emp(dev_2)
mgr1.print_emps()
mgr1.remove_emp(dev_1)
mgr1.print_emps()


print(isinstance(dev_1,Employee))
print(isinstance(emp_1,Manager))

print(issubclass(Developer,Employee))
print(issubclass(Employee,Manager))