#import math
from math import sqrt as ibmsqrt
bad_data = True
while bad_data == True:
    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
        bad_data = False
    except:
        print('Вы ввели плохие данные!!')
D = b * b - 4 * a * c
print('Дискриминант равен {}'.format(D))
if D < 0:
    print('Уравнение не имеет корней')
elif D == 0:
    x1 = -b / (2 * a)
    print(f'Уравнение имеет один корень: X1 = {x1}')
else:
    x1 = (-b + ibmsqrt(D)) / (2 * a)
    x2 = (-b - ibmsqrt(D)) / (2 * a)
    print(f'Уравнение имеет два корня: X1 = {x1}, X2 = {x2}')
