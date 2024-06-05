#constructor
class Employee:
    def __init__(self, id, name):#parametric
        self.id = id
        self.name = name

    def display(self):#non-parametric
        print("Id", self.id)
        print("Name", self.name)

emp1 = Employee(1, "john")
anu = Employee(2, "Anu")
emp1.display()
anu.display()