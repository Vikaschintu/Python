p=4.95
i=5
while p<25:
    d=p*60/100
    ap=p-d
    print('Product amount {} discount amount {} product price after discount{}'.format(p,d,ap))
    p=p+i