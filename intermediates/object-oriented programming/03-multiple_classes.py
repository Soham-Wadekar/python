class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:

    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        
        average = 0
        for student in self.students:
            average += student.get_grade()
        return average / len(self.students)          

s1 = Student("Soham", 20, 95)
s2 = Student("John", 18, 45)
s3 = Student("Bob", 23, 75)

course = Course("Engineering", 2)
course.add_student(s1)
course.add_student(s2)
print(f"The first student is {course.students[0].name}")
print(f"The average grade of all the students in the course is {course.get_average_grade()}")