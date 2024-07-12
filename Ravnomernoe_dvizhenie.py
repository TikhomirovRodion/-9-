import time

V=float(input('Скорость (м/с): '))
tkon=float(input('Время (с): '))
t=0
S=0
V=V*10
tkon=tkon*10
while t<tkon:
    time.sleep(0.1)
    t+=1
    S = V*t
    print('Время: ',t/10,' с, ','расстояние: ',S/100,' м')
