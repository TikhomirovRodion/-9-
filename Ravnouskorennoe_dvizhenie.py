import time

Xnach=float(input('Начальное положение (м):'))
Vnach=float(input('Начальная скорость (м/с): '))
MnogoV=float(input('Ускорение (м/с2): '))
tkon=float(input('Время (с): '))

V=Vnach
t=0
X=0

while t<tkon:
    time.sleep(0.1)
    t+=0.1
    X=Xnach+Vnach*t+(MnogoV*t**2)/2
    V+=MnogoV/10
    if V*100//10<5:
        V=int(V*10)
        V/=10
    else:
        V=int(V*10)+1
        V/=10
    if t*100//10<5:
        t=int(t*10)
        t/=10
    else:
        t=int(t*10)+1
        t/=10
    print('X=',int(X*100)/100,'м ','Скорость: ',V,'м/с ','Время: ',t,'c')
