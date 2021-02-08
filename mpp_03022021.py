

class Person:
    birthday = '00-00-0000'
    address = []

    def __init__(self, name, last_name, dni):
        self.name = name
        self.last_name = last_name
        self.dni = dni

    def get_full_name(self):
        return f"{self.name} {self.last_name}"
    
    def getDay(self):
        day_birthday = self.birthday.split('-')
        return day_birthday[0]
    
    def getMonth(self):
        month_birthday = self.birthday.split('-')
        return month_birthday[1]
    
    def getYear(self):
        year_birthday = self.birthday.split('-')
        return year_birthday[2]
        

    def __str__(self):
        return f"{self.name} {self.last_name} was born on {self.birthday}"


obj1 = Person('Kandjigar', 'the destroyer', 'M-010101_O')
obj2 = Person('Drax', 'the destroyer', 'M-010102_O')
obj3 = Person('Aargamon', 'the pacifist', 'M-010102_O')

list__ = [obj1, obj2, obj3]
lista = [i.__dict__['name'] : i.__dict__['last_name'] for i in list__]
#for i in list__:
#    print(i.__dict__['name'])
print(lista)
"""
dataBase = open('data.txt', 'wb')
dataBase.write(obj1)
dataBase.close()

reBase = open('data.txt','r')
message = reBase.read()
print(message)
reBase.close()
"""

#import pickle
"""
lis_Tt = [obj1, obj2]
with open("data.txt", "wb") as f:
    pickle.dump(lis_Tt, f)

"""

"""
with open("data.txt", "rb") as f:
    obj = pickle.load(f)

check_list = []
for i in obj:
    check_list.append(i.__dict__)
if obj3.__dict__ in check_list:
    print(True)
else:
    print(False)
#print(obj)
"""

"""
import re

text = 'this is a text chain'
print(text.find('bro'))

searh_ = re.search('chain', text)
print(searh_)
"""
#l = [1,2,4,'op']
#b = 'op'
#if l.__contains__(b):...
#print(dir(str))
#repr(l)