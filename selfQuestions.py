#Self parameter purpose it is to represent the instance of the class and,
# allow every method in the class to access the important instance variable,
#  unlike class every it is the same with all instances of the class.

#You use the self parameter in methods inside a class after constructor

#Constructor is require sself parameter because,
#  you use self parameter to create instace variables and,
#  constructor is made to make instance variables and,
#  be called everytime instance of the class is made

# If you don't put self parameter in an constructor, it will give an error.

#there would be no way to distinguish which
#  instance's attributes and methods should be accessed,
#  leading to conflicts or errors.

# we see "None" when printing a method that does not have a return type because,
# the method can't return anything because, there is no return function

class Myclass():
    i = "This is a class variable"
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def hello(self):
        print(self.x,self.y,Myclass.i)

#This where we create defining value for instance variables for first object
class1 = Myclass(1,2)
#This where we create defining value for instance variables for second object
class2 = Myclass("variable 1","variable 2")

#this is a method from the first object
class1.hello()
#this is a method from the second object
class2.hello()


#Local variable is a variable created in a method where only the method can access it.


# difference between class variable and instance variable is, that the
# class variable is created in the class and is the same for all instances of the class.
# Instance variable is created in the constructor after "self" and
# is different to all objects of classes.