class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student:
    def __init__(self, rollno):
        self.rollno = rollno
    def getRollno(self):
        print(self.rollno)

class Resident(Person, Student):
    def __init__(self, name, age, rollno):
        Person.__init__(self, name, age)
        Student.__init__(self, rollno)

r = Resident("Roshan", 21, 101)
r.showName()
r.showAge()
r.getRollno()