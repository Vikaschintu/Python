x=float(input('Enter x coordinator: '))
y=float(input('Enter y coordinator: '))
a=list()
b=list()
count=0
while x!=0:
    x=float(input('Enter x coordinator: '))
    y=float(input('Enter y coordinator: '))
    count=count+1
    a.append(x)
    b.append(y)
i=sum(a)*sum(b)-sum(a)*sum(b)/count
j=sum(a)**2-sum(a)**2/count
m=i/j
avga=sum(a)/count
avgb=sum(b)/count
d=avgb-m*avga
print(avga,avgb,d,m)
print("y={}x+{}".format(m,d))
    

    