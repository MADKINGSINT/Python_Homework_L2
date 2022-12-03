# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
#  в одной строке одно число.


def sp(n):
    list = []
    for i in range(-n , n+1):
        list.append(i)    
    return list
print (list)
N = int(input('Введите N: '))
numbers = sp(N)
print(numbers)
x = open('HomeworkL2/file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)