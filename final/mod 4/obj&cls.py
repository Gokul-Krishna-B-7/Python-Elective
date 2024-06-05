class Student:
    def fill_details(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print("A student detail object is created...")

    def print_details(self):
        print("Name: ", self.name)
        print("Branch: ", self.branch)
        print("Year: ", self.year)

s1 = Student()
s2 = Student()

s1.fill_details('Rahul','CSE','2020')
# A student detail object is created...
s1.print_details()

s2.fill_details('Akhil','ECE','2010')
# A student detail object is created...
s2.print_details()
