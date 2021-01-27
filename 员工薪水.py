a=int(input("请输入员工的销售额:"))
if a<= 3000:
    print("该员工的薪资为{}:".format(a))
elif 3000<a<=7000:
    a=a+0.1*a 
    print("该员工的薪资为{}:".format(a))
if 7000<a<=10000:
    a=a+0.15*a
    print("该员工的薪资为{}:".format(a))
elif 10000<a:
    a=a+0.2*a
    print("该员工的薪资为{}:".format(a))


    


    
    

