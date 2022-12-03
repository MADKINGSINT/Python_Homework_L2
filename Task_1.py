
#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#     Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = (input("Введите вещественное число:  "))
i = (len(number))
answer = 0
for x in range (0 , i ):
    if number[x].isdigit() == True:
        answer += int(number[x])
    x +=1
print(answer)