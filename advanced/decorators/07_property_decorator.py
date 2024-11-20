'''
`property` decorator adds the functionality of a getter, setter and deleter to a function and allows the object to treat the function like an attribute
'''

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, fullname):
        first, last = fullname.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f"Deleting {self.fullname}")
        self.first, self.last = None, None
    
emp_1 = Employee("Dwight", "Schrute")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

emp_1.first = "Dwayne"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

emp_1.fullname = "Jim Halpert"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

del emp_1.fullname

print(emp_1.first)
print(emp_1.last)
