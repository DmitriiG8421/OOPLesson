# inheritance is mechanism when
#  your create a sub class to take the methods and
#  class variables from the super class


#You create a subclass by write 'class' then the subclass's name,
#  then in brackets you write the superclass's name


#superclass is like a parent class, superclass is the nornal class before you inherit it. 
# When you inherit the normal class it is called a 'superclass'


#The concept of code reuse with respect to inheritance is
# when we use the methods from the superclass in the subclass


#You can call a method form a superclass in a subclass by,
# just calling it using an object of the subclass


#The super() function is used to give access to methods
#  and properties of a parent or sibling class


#Yes, a subclass can have its own metho in addiction t the inherited ones.
class Door():
    def __init__(self):
        pass
    def doorOpening(self):
        print("creeeeeeek")
class electricDoor(Door):
    def __init__(self):
        pass
    def safetyFeature(self):
        print("Please enter the password")

x = electricDoor()
x.doorOpening()
x.safetyFeature()


# The term "method overriding" in Python inheritance is when you crete a method 
# in a subclass with the same name with the method in the superclass and,
# you make it do something else.

