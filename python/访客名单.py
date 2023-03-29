while True:
    name = input("请输入您的姓名：")
    if name == 'quit':
        break
    print(f"欢迎您的访问{name}")
    with open('guest_book.txt','a') as file:
        file.write(f"{name}\n")