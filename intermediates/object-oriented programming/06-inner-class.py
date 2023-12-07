class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print(f"Name: {self.name} , Roll No: {self.roll_no}")

    class Laptop:  # INNER CLASS
        def __init__(self):
            self.brand = "Lenovo"
            self.cpu = "i5"
            self.ram = 16


s1 = Student("Bob", 10)
s2 = Student("Tim", 31)

s1.show()

print(s1.lap.brand)

l1 = Student.Laptop()
print(l1.cpu)
