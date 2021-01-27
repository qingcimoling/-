flie_name = input ("请输入要备份的文件名字:")
source_file = open(flie_name,"r")
if source_file:
    flag = flie_name.rfind(".")
    if flag >0:
        copy_file =flie_name[:flag] + "[备份]" + flie_name[flag:]
    new_file =open(copy_file,"w")
    for line_content in source_file.readlines():
        new_file.write(line_content)
source_file.close()
new_file.close()