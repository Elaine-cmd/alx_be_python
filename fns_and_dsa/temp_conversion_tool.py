class Student:
    def __init__ (self, name, age ):
        self.name = name
        self.age = age

    def display_information (self):
        print(f" Student name: {self.name}")
        print(f"Student age: {self.age}")

    student1 = Student("Alice", 20)
    student2 = Student("Einstein", 19)
     
    print("Displaying information for student1:")
    student1.display_info()
    print("Displaying information for student2:")
    student2.display_info()

  




















































