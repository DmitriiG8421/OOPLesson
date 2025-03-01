class Animal:
  #class variables/attributes/properties
  legs = 4
  ears = 2
  eyes = 2
  #behaviours
  def make_sounds(self): # self mush be the first parameter for a method defined in a class
      print("This animall makes some sound!")

class House:
  windows = 8
  doors = 3
  bathroom = 2.5

african_elephant = Animal() #instance of a class (Animal)
print("African elephant has",african_elephant.ears,"ears")
african_elephant.make_sounds()

asian_elephant = Animal() 
print("Asian elephant has",asian_elephant.ears,"ears.")
asian_elephant.make_sounds()




b = "python" #string
print(b.capitalize()) # this is a behavour of string class


#Everything is an object
a = "10"
print(type(a))