# 1. a constructor is a method which is called automatically
# every time an object of a class is created.
# Mainly used to initialise the instance variable
class class1:
    # This is a constructor
    def __init__(self):
        print("This is an example of a constructor!")
        #This is a method

    def good_morning(self):
        print("Good morning friend!")

#Making an object of the class
classExample = class1()
#calling a method
classExample.good_morning()


# 2. difference between class variable and instance variable is, that the
# class variable is created in the class and is the same for all instances of the class.
# Instance variable is created in the constructor after "self" and
# is different to all objects of classes.


# 3. A generic method is needed to be called explicitly, constructor is automatically called,
# when an object of the class is created.
#Also, constructors are important for OOP coding and for instance variable.


# 4.
class characterIronMan():
    #These are class variables
    arms = 2
    legs = 2
    suitNumber = "Mark 42"

    #I am creating the constructor
    #"age" and "gender" are the parameters
    #  that we need to define when creating an object of the class
    def __init__(self, age, gender):
        #These are instance variables
        self.age = age
        self.gender = gender
        #This line will be printed when an object the class is created
        print("Iron man is waking up!")


    #This is just a normal class method with a class variable
    def callingSuit(self):
        print("Suit is called with",youngIronMan.arms,"arms!")


    # This is a method too but, it also uses class variables and instance variables
    # Instance variables are binded to the instance of the class
    # And you can access class variables anywhere
    def introducing(self):                     #These are class variables
        print("The young Iron Man has", youngIronMan.arms, "arms,", youngIronMan.legs,
              "legs,", youngIronMan.suitNumber,"and is", self.gender, "and", self.age, "years old!")
                                                        #These are an instance variable


#This is an object of our class
# "11" and "male" are the arguments that we need to define           
youngIronMan = characterIronMan(11,"male")

#This is the method in which we used the class and instance variables
youngIronMan.introducing()

#This is the method in which we used only class variables
youngIronMan.callingSuit()




# 5. True, constructor is a special method and is called every time an object is created, called init

# 6. False, class variables are always the same for all objects of the class.

# 7. True, the self parameter is used in Python classes to refer to the class itself.

# 8. False, if you change an instance variable it only changes for that instance of a class.