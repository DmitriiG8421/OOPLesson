class Animal:
  #class variables/attributes/properties
  legs = 4
  ears = 2
  eyes = 2

class House:
  windows = 8
  doors = 3
  bathroom = 2.5

african_elephant = Animal() #instance of a class (Animal)
print("African elephant has",african_elephant.ears,"ears")
asian_elephant = Animal() 
print("Asian elephant has",asian_elephant.ears,"ears.")


#Everything is an object
a = "10"

print(type(a))