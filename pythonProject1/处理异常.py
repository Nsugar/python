print("Give me two numbers,and I'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input ("\n First number: ")
    if first_number == 'quit':
        break
    second_number = input("Second_number:")
    if second_number == 'quit':
        break
    try:
        answer = int(first_number) / int(second_number)
    except:
        print("You can't divide by 0!")