class Parent:
    def func1(self):
        print("This function is in Parent")

class Child1(Parent):
    def func2(self):
        print("This function is in Child1")

class Child2(Parent):
    def func3(self):
        print("This function is in Child2")

c1 = Child1()
c2 = Child2()

c1.func1()
c1.func2()

c2.func1()
c2.func3()