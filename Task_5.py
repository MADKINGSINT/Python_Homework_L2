# Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).
from random import randint
ListSize = int(input('Введите размер списка:   '))
sp = []

for i in range (0, ListSize):
    sp.append(int(input('Введите число: ')))

print(sp)
def RandomizeList (sp):
    for i in range (0, len(sp)):
        
        x = randint(i, len(sp)-1)
        y = randint(i, len(sp)-1)
        sp[x], sp[y] = sp[y], sp[x]
           
        i+=1 
      
RandomizeList(sp)
print(sp)
        








