class Cat:
    name=""
    color=""
    weight=0
    def meow(self):
        print(self.name, "сказала мяу")
mycat=Cat()
mycat.name="Луна"
mycat.color="Серый"
mycat.weight=3
mycat.meow()
print()

class Animal:
    name=""
    def __init__(self,newname):
        self.name=newname
        print("Родилось животное", self.name)
    def eat(self):
        print("Ням-ням")
    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname
    def makeNoise(self):
        print(self.name,"говорит Гррр")
Animal=Animal("Солнце")
Animal.eat()
Animal.getName()
Animal.setName("Марс")
print(Animal.getName())
Animal.makeNoise()
print()

class StringVar:
    znach="значение"
    def get(self):
        return self.znach
    def set(self,newznach):
        self.znach=newznach
s=StringVar()
print(s.get())
s.set("Новое значение")
print(s.get())
print()

class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def get(self):
        print(self.x, self.y)
    def move(self, dx, dy):
        '''Determines where x and y move'''
        self.x = self.x + dx
        self.y = self.y + dy

a=Point(1,1)
b=Point(5,2)
print("Объявляем переменные")
a.get()
b.get()
print("Перемещаем переменные")
a.move(2,2)
b.move(6,6)
a.get()
b.get()

        
        
        
