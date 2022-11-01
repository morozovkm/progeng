# import math
from math import sqrt

bad_data = True
while bad_data == True:

    try:
        a = int(input('введите первое число:'))
        b = int(input('введите второе число:'))
        c = int(input('введите второе число:'))
        bad_data = False
    except:
        print('вы ввели не число!!!')

D = b * b - (4 * a * c)

print(f'Дискриминант равен {D}')
if D < 0:
    print('Уравнение не имеет корней')
elif D == 0:
    x = (-b) / (2 * a)
    print(f'уравнение имеет один корень, x1={x1}')

else:
    x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) + sqrt(D)) / (2 * a)
    print('Уравнение имеет 2 корня х1 = {x1}, x2 = {x2}')
