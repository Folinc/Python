# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
number_S = int(input("Введите сумму чисел S: "))
number_P = int(input("Введите произведение чисел P: "))
for x in range(number_S):
    for y in range(number_P):
        if number_S == x + y and number_P == x * y:
            print("число Х:", x, "Число Y:", y)
