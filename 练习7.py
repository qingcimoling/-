list1=[]
str1="XinYu"
tup1=1,2,3,4,5


a=list(str1)
b=list(tup1)
list1=a+b
print(list1)


list1+=str1
print(list1)


list1[5:10]=[]
print(list1)

d="".join(list1)
print(d)


e=tuple(d)
print(e)