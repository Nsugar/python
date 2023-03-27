#披萨配料
# while True:
#     topping = input("请输入您所需要的配料：")
#     if topping == 'quit':
#         break
#     print(f"我们将会在披萨的配料中添加{topping}")

#电影票
# pay = 0
# while True:
#     user_age = input("请输入你的年龄：")
#     if user_age == 'quit':
#         break
#     user_age = int(user_age)
#     if user_age < 3:
#         pay = 0
#     elif user_age <= 12:
#         pay = 10
#     else:
#         pay = 15
#     print(f"你的票价为{pay}美元")

#在列表之间移动元素
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("\nVerifying users have been confirmed:")
#     confirmed_users.append(current_user)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#删除为特定值的所有列表元素
# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# while 'dog' in pets:
#     pets.remove('dog')
# print(pets)

#使用用户输入来填充字典：
responses = {}
while True:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        break