
m=int(input('Enter number of minutes: '))
s=int(input('Enter number of text messages: '))
mb=15.00
a=m-50
b=m-50
ec=a*0.25
em=b*0.15
tb=ec+em+mb
tm=ec+mb
ts=em+mb
if m<=50 and s<=50:
    print('The bill amount is $',mb)
elif m>50 and s>50:
    print('The bill amount is $',tb)
elif m>50 and s<=50:
    print('The bill amount is $',tm)
elif m<=50 and s>50:
    print('The bill amount is $',ts)
    
