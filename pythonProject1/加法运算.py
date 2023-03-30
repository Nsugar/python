while True:
    number1 = input('请输入一个数：')
    number2 = input('请再输入一个数： ')
    if number1 == 'quit' or number2 == 'quit':
        break
    try:
        number1 = int(number1)
        number2 = int(number2)
    except:
        print('您输入的是文本而不是数字，请输入数字')
    else:
        print(number1 + number2)
