# class Animal:
#     def make_sound(self,s):
#         print(s)
# class Horse(Animal):
#     pass
#
# mustang = Horse()
# mustang.make_sound('chert')

#
# class Gaishnik:
#     def kruti_pedali(self,f):
#         print(f)
# class Hirasima(Gaishnik):
#     print('sobbe')
#
# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class Super_car(Car):
#     def __init__(self,model,color,year,sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor
#
# class PR1:
#     pass
# class Pr2:
#     pass
# class Child(PR1,Pr2):
#     pass
#
# class MY_class:
#     def __init__(self,value):
#         self.value = value
#     @classmethod
#     def from_sting(cls,string):
#         return cls(int(string))
#
# check = MY_class.from_sting('10')
# print(type(check.value))
#
# class rere:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     @property
#     def area(self):
#         return self.width * self.height
# rect = rere(4 , 5)
# print(rect.area)
# rect.width = 6
#
# class Standart_Worker:
#     def __init__(self,name , job ):
#         self.name = name
#         self.job = job
#
#
# class HR(Standart_Worker):
#     pass

class Player:
    def __init__(self,speed,stamina,power,accuracy):
        self.speed = speed
        self.stamina = stamina
        self.power = power
        self.accurancy = accuracy

class striker:
    def __init__(self,speed,stamina,power,accuracy):
        super().__init__(speed,stamina,power,accuracy)
    def catch(self):
        print('ударил мяч')
class goalkeeper:
    def __init__(self, speed, stamina, power, accuracy):
        super().__init__(speed,stamina,power,accuracy)


class defencer:
    def __init__(self, speed, stamina, power, accuracy):
        super().__init__(speed,stamina,power,accuracy)

class half_defenser:
    def __init__(self, speed, stamina, power, accuracy):
        super().__init__(speed,stamina,power,accuracy)


