class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

student1 = Student(name, age, course)

print("Student Details:")
student1.display_info()
