#import math
#from math import sqrt as  ibmsqrt (замена имени функции на свою)

bad_data = True
while bad_data == True:
    try:
        a = int(input('Введите а:'))
        b = int(input('Введите b:'))
        c = int(input('Введите c:'))
        bad_data = False
    except:
        print('Вы ввели плохие данные !!!')

D = b * b - (4 * a * c)
print(f' Дискриминат равен {D}')
if D < 0:
    print('Уравнение не имеет корней')
elif D == 0:
    x1 = (-b) / (2 * a)
    print(f'Уравнение имеет один корень X1={x1}')
else:
    x1 = ((-b) + math.sqrt(D)) / (2 * a)
    # x1 = ((-b) + sqrt(D)) / (2 * a)
    x2 = ((-b) - math.sqrt(D)) / (2 * a)
    print(f'Уравнение имет 2 корня: X1={x1}, X2={x2}')

