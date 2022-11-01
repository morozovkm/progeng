import math
bad_data = True
while bad_data == True:
    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
        bad_data = False
        d = b*b - 4*a*c
        if d > 0:
            print('уравнение имеет два корня')
            x1 = (-b - math.sqrt(d))/(2*a)
            x2 = (-b + math.sqrt(d))/(2*a)
            print(x1, x2)
        elif d == 0:
            print('уравнение имеет один корень')
            x = -b/(2*a)
            print(x)
        else:
            print('Уравнение не имеет решения')
    except:
        print('Вы ввели неверные данные')
