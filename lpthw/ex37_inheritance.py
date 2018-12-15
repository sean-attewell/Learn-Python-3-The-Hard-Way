# Inheritance enable us to define a class that takes all the functionality
# from parent class and allows us to add more.

# The new class is called derived (or child) class and the one from which 
# it inherits is called the base (or parent) class.

# class BaseClass:
  #Body of base class
#class DerivedClass(BaseClass):
  #Body of derived class

# Derived class inherits features from the base class,
# adding new features to it. This results into re-usability of code.  

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)] # as it sounds
        # in a list because of square brackets! 

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
        # Makes the user input the length of each side to populate the
        # self.sides list 

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

# instantiate an instance (the object square)
square = Polygon(4)

# Initialised with these two attributes which we can print.
print(square.n)
print(square.sides)

square.inputSides()

print(square.sides)

square.dispSides()

print("\n\n")

# This class has data attributes to store the number of sides, n 
# and magnitude of each side as a list, sides.

# Method inputSides() takes in magnitude of each side and similarly, 
# dispSides() will display these properly.

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is: ', area)

# A triangle is a polygon with 3 sides. So, we can created a class 
# called Triangle which inherits from Polygon. This makes all the 
# attributes available in class Polygon readily available in Triangle. 
# We don't need to define them again (code re-usability). 

# However, class Triangle has a new method findArea() 
# to find and print the area of the triangle.

t = Triangle()

t.inputSides()

t.dispSides()

t.findArea()

# We can see that, even though we did not define methods like 
# inputSides() or dispSides() for class Triangle, we were able to use them.

# If an attribute is not found in the class, search continues to the base
# class. This repeats recursively, if the base class is itself derived
# from other classes.

########### Method Overriding in Python ################

# In the above example, notice that __init__() method was defined in both
# classes, Triangle as well Polygon. When this happens, the method in
# the derived class overrides that in the base class. This is to say,
# __init__() in Triangle gets preference over the same in Polygon.

# Generally when overriding a base method, we tend to extend the 
# definition rather than simply replace it. The same is being done by
# calling the method in base class from the one in derived class 
# (calling Polygon.__init__() from __init__() in Triangle).

# A better option would be to use the built-in function super(). 
# So, super().__init__(3) is equivalent to Polygon.__init__(self,3) 
# and is preferred.

print("\n\n")

# Two built-in functions isinstance() and issubclass() are used to check
# inheritances. 
# 
# Function isinstance() returns True if the object is an
# instance of the class or other classes derived from it. 
# Each and every class in Python inherits from the base class object.

print(isinstance(t,Triangle))

print(isinstance(t,Polygon))

print(isinstance(t,int))

print(isinstance(t,object))

print("\n\n")

# Similarly, issubclass() is used to check for class inheritance.

print(issubclass(Polygon,Triangle))

print(issubclass(Triangle,Polygon))

print(issubclass(bool,int))

