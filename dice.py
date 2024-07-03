import random
class Dice:
    def roll(self):
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        print(num1,num2)
num=Dice()
num.roll()