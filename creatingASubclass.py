class Bird():
    tail = 1
    eyes = 2
    name = "Liger"
    def __init__(self, feather_color):
            self.feather_color = feather_color

    def method1(self, hands, ears):
            total = hands + ears
            return total
    def method2(self):
            print(f"nand the hair color is: {self.feather_color}")

class Parrot(Bird):

        def __init__(self,wings,feather_color,tail):
              self.wings = wings



        def fly(self,wings):
               print("Liger is flying using", wings,"wings.")

        def copyVoice(self):
               phrase = input("The parrot will copy-")
               print("Parrot said '"+phrase+"'")


x = Parrot(2,"green",1)
x.fly(x.wings)
print(x.method1(x.tail,x.wings))
x.copyVoice()