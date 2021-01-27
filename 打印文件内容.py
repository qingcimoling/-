new = []
file=open("aaa.txt", "r")
contents = file.readlines()
for ele in contents :
    if ele.startswith("#")==False:
        new.append(ele)
print(new)
file.close()