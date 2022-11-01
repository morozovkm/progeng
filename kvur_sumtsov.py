import math
bad_data = True
while bad_data == True:
    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
        bad_data = False
    except:
        print('Вы ввели плохо данные!')

D = b * b - (4 * a * c)
print(f'Дискриминант равен {D}')

if D < 0:
    print('Уравнение не имеет корней')
elif D == 0:
    x1 = (-b) / (2 * a)
    print(f'Уравнение имеет один корень, x1={x1}')
else:
    x1 = ((-b) + math.sqrt(D)) / (2 * a)
    x2 = ((-b) - math.sqrt(D)) / (2 * a)
print(f'Уравнение имеет 2 корня X1 = {x1},X2 = {x2}')
