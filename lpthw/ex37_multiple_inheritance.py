#### Multiple Inheritance in Python ####

# https://www.programiz.com/python-programming/multiple-inheritance

# Like C++, a class can be derived from more than one base classes in 
# Python. This is called multiple inheritance.

# In multiple inheritance, the features of all the base classes are 
# inherited into the derived class. The syntax 
# for multiple inheritance is similar to single inheritance.

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

# Here, MultiDerived is derived from classes Base1 and Base2
# Has its own features as well as those of both base classes. 


#### Multilevel Inheritance in Python ####

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

# This is called multilevel inheritance. It can be of any depth in Python.
# In multilevel inheritance, features of the base class and the
# derived class are inherited into the new derived class.

# Here, Derived1 is derived from Base, and Derived2 is derived from 
# Derived1.

# Derived2 has its own features, as well as those of Derived 1 and base


####### Method Resolution Order in Python #########

# Every class in Python is derived from the class object. It is the most
# base type in Python. So technically, all other class, either built-in
# or user-defined, are derived classes and all objects are instances of
# object class.

# In the multiple inheritance scenario, any specified attribute is
# searched first in the current class. If not found, the search continues
# into parent classes in depth-first, left-right fashion without searching
# the same class twice.

# So, in the above example of MultiDerived class the search order is 
# [MultiDerived, Base1, Base2, object]. This order is also called 
# linearization of MultiDerived class and the set of rules used to find
# this order is called Method Resolution Order (MRO).

# It ensures that a class always appears before its parents and in case 
# of multiple parents, the order is same as tuple of base classes.

# Mathematicians usually write tuples by listing the elements within 
# parentheses and separated by commas; for example, (2, 7, 4, 1, 7) 
# denotes a 5-tuple

# MRO of a class can be viewed as the __mro__ attribute or mro() method. 
# The former returns a tuple while latter returns a list.

print(MultiDerived.__mro__)

print(MultiDerived.mro())

print("\n\n")

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())

# Why B before A? 


