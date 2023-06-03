# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
stop = int(input("Введите число N:"))
count = 0
while count ** 2 <= stop:
    print(count ** 2)
    count += 1
