import random as r
a=0
d=0
e=0
f=0
for g in range(50):
    for i in range(5):
        b=r.randint(1,6)
        a=a+b
    for i in range(5):
        c=r.randint(1,6)
        d=d+c
    if a>d:
        e=e+1
    elif a<d:
        f=f+1
if e>f:
    print("最终获胜者为玩家一")
elif e<f:
    print("最终获胜者为玩家二")
    




    



