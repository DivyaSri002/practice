class Person:
    def __init__(self,name):
        self.name=name
        pass
    def talk(self):
        print(f"Hi {self.name}")
x=Person("Divya")
print(x.name)
x.talk()