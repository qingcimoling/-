def num_sum(*num):
    a=0
    for i in range(len(num)):
        a+=num[i]
    return a

num = (1,2,3,4)
b= num_sum(num)
print(b)

