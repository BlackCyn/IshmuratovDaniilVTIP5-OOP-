#Создайте класс Cat. Определите атрибуты name, color, weight
#Добавьте метод под названием  meow. Создайте объект класса Cat, установите атрибуты, вызовите метод meow
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

#Напишите код, описывающий класс Animal:
#добавьте атрибут имени животного
#добавьте метод eat выводящий "Ням-ням"
#добавьте метод getName setName
#добавьте метод makeNoise, выводящий "Имя животного говорит Грр"
#добавьте конструктор классу Animal. выводящий "Родилось новое животное Имя эивотного"
#
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

#Создайте класс StringVar для работы со строковыми тимов данных, содержащий
#методы set get. метод set сулжит для изменения содержимого текста
#get-для получения содержимого текста
#создайте объект типа StringVar и протестируйте его методы
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

#Создайте класс точка Point, позволяющий работать с координатами (x,y).
#Добавьте необходимые методы класса
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

        
        
        
