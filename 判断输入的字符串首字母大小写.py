def is_capital(a) :
    if ord("A")<=ord(a[0])<=ord("Z"):
        return "首字母是大写的"
    else:
        return "首字母是小写的"
words=input("请输入想要判断的字符串")
result = is_capital(words)
print(result)

