
y=int(input('Enter year: '))
m=int(input('Enter month: '))
d=int(input('Enter date: '))
ny=y+1
nm=m+1
nd=d+1
lp=y%400
lp1=lp%100
lp2=lp1%4
m31=list[1,3,5,7,9,11,12]
m30=list[4,6,8,10]
m28=list[2]
if (m in m31) and m==31:
    print(y,nm,1)
elif (m in m30) and m==30:
    print(y,nm,1)
elif lp2==0 and m==2 and d==29:
    print(y,nm,1)
elif (m in m31) and m<31:
    print(y,m,nd)
elif (m in m30) and m<30:
    print(y,m,nd)
elif m==12 and d==31:
    print(ny,1,1)
elif (m in m28) and m==28:
    print(y,nm,1)
elif lp2!=0 and m==2 and d==28:
    print(y,nm,1)
else:
    print(y,m,nd)
