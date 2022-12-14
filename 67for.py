x=int(input('Enter x value: '))
y=int(input('Enter y value:'))
if x=='':
    print('Input error')
else:
    while x!='':
        p=x*y
        o=p+p
        x=int(input('Enter x value (Leave blank to exit): '))
        y=int(input('Enter y value:'))
print(o)
        
    