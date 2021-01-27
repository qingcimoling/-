def fanta(n,A,B,C):
    if n == 1:
        print(A, '->',C)
    else: 
        fanta(n-1,A,C,B)
        print(A, '->',C)
        fanta(n-1,B,A,C)


fanta(3,"X","Y","Z")