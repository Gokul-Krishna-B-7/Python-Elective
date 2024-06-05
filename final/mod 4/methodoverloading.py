class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Rectangle:", a * b)
        elif a != None:
            print("square:", a * a)
        else:
            print("No figure assigned")

obj1 = Area()
obj1.find_area()
obj1.find_area(5)   
obj1.find_area(45,55)