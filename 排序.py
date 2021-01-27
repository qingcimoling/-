file = open("digit.txt","r")
content = list(file.read())
content.sort()
print(content)