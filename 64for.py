
p=4.95
for i in range(0,30,5):
    d=p*60/100
    ap=p-d
    print('Product amount {} discount amount {} product price after discount{}'.format(p,d,ap))
    p=p+i