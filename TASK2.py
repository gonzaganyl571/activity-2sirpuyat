class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Creating student objects
student1 = Student("Charlotte", 17, "Information technology")
student2 = Student("Jaymark", 18, "Information technology")
student3 = Student("Jessica", 19, "Information technology")

# Introducing students
student1.introduce()
student2.introduce()
student3.introduce()