def f(a):
    a1_num=0
    letter_num = 0
    space_num = 0
    other_num = 0
    for n in a:
        if n.isdigit()==True:
            a1_num +=1
        elif n.isalpha()==True:
            letter_num +=1
        elif n.isspace()==True:
            space_num += 1
        else:
            other_num += 1
    return a1_num,letter_num,space_num,other_num
h=input("输入一个字符串:")
b=f(h)
print("数字字符数:","字母字符数:","空格字符数","其他类型字符数:",b)
