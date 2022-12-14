
m=float(input('Enter the Magnitude: '))
if m<2.0:
    print('Micro')
elif m==2.0 or m<3.0:
    print('Very Minor')
elif m==3.0 or m<4.0:
    print('Minor')
elif m==4.0 or m<5.0:
    print('Light')
elif m==5.0 or m<6.0:
    print('Moderate')
elif m==6.0 or m<7.0:
    print('Strong')
elif m==7.0 or m<8.0:
    print('Major')
elif m==8.0 or m<10.0:
    print('Great')
else:
    print('Meteoric')