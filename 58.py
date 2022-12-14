
y=int(input('Enter a year: '))
d=y%400
d1=d%100
d2=d1%4
if d==0:
    print('Leap Year')
elif d1==0:
    print('Not a Leap year')
elif d2==0:
    print('Leap year')
else:
    print('Not a leap year')