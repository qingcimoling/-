import math as m 
a = int (input('请输入一个数:'))
if a > 0:
    print("这个数的绝对值是{}".format(a))
elif a < 0:
    b = m.fabs(a)
    print("这个数的绝对值是{}".format(b))