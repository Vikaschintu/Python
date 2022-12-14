n=int(input('Enter your age of guests: '))
if n=='':
    print('Error')
elif n<=2:
    c1=0
elif n>=3 and n<=12:
    c2=14
elif n>=13 and n<=64:
    c3=23
elif n>=65:
    c4=18
else:
    while n!=0:
        n=int(input('Enter your age of guests: '))
x=c1+c2+c3+c4
print(x)

        
        