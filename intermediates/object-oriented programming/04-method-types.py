class Student:

    school = "XYZ"              # Static / Class Variable (Define outside the constructor)

    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def get_avg_marks(self):    # INSTANCE METHOD
        return round((self.marks1 + self.marks2 + self.marks3)/3, 2)
    
    def get_marks1(self):       # ACCESSOR METHOD / GETTER
        return self.marks1
    
    def set_marks1(self, val):  # MUTATOR METHOD / SETTER
        self.marks1 = val

    @classmethod
    def get_school(cls):        # CLASS METHOD
        return cls.school
    
    @staticmethod               # STATIC METHOD
    def info():
        return "This class is an example to understand the different method types used!"

s1 = Student(31,59,65)          # Instance Variable
s2 = Student(94,83,99)

print(s1.get_marks1())
s1.set_marks1(80)
print(s1.marks1)

print(s1.get_avg_marks())

print(Student.get_school())

print(Student.info())