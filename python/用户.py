name = input("请输入您的用户名")
filename = 'user.txt'
with open(filename,'w') as file:
    file.write(name)