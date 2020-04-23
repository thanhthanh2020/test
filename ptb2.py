import math
print('Day la chuong trinh giai phuong trinh bac 2')
a = int (input('a = '))
b= int (input('b = '))
c= int (input('c = '))
delta = b*b-4*a*c
if delta > 0:
    print('Phuong trinh co 2 nghiem phan biet: ') 
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
elif delta == 0:
    print('Phuong trinh co nghiem kep: ')
    x = -b/(2*a)
    print('x = ' + str(x))
else:
    print('Phuong trinh vo nghiem')