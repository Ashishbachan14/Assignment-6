'''Write a Python program to create two empty classes, Student and Marks. Now create
some instances and check whether they are instances of the said classes or not. Also,
check whether the said classes are subclasses of the built-in object class or not.'''

class Student:
    pass

class Marks:
    pass

Ashish=Student()

Ashish_ke_marks=Marks()

print("Ashish is an instance of class Student:",isinstance(Ashish,Student))
print("Ashish is an instance of class Marks:",isinstance(Ashish,Marks))
print("Ashish_ke_marks is an instance of class Student:",isinstance(Ashish_ke_marks,Student))
print("Ashish_ke_marks is an instance of class Marks:",isinstance(Ashish_ke_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))
