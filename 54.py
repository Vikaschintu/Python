
r=float(input('Enter rating of employee: '))
a=2400*r
if r==0.0:
    print('Unacceptable Performance')
    print('The amount of the employee raise is $',a)
elif r==0.4:
    print('Acceptable Performance')
    print('The amount of the employee raise is $',a)
elif r>=0.6:
    print('Meritorious Performance')
    print('The amount of the employee raise is $',a)
else:
    print('Error')