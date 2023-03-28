# def greet_user():
#     """显示简单问候语"""
#     print("Hello Python!")
# greet_user()
def greet_user(user_name):
     """显示简单问候语"""
     print(f"Hello {user_name}, I love you")

greet_user('zhao yixu')

def display_message():
    print("这一章我学习的是函数")

display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title} in Wonderland")

favorite_book('hai zeiwang')

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog','zhu fengyuan')
describe_pet(animal_type = 'dog',pet_name = 'zhu fengyuan')

def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

#返回字典

def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

#城市名
def city_country(city_name,country_name):
    message = f"{city_name}, {country_name}"
    return message
test1 = city_country(city_name = 'henan',country_name = 'china')
test2 = city_country('beijing','china')
test3 = city_country('luosanji','American')

#专辑
# def make_album(people_name,zhuanji,count = None):
#     message = {'name':people_name,'ge':zhuanji}
#     if count:
#         message['count'] =count
#     return message
# test1 = make_album('zhao yixu','I only love you',5)
# print(test1)
# while True:
#     name = input("请输入你喜欢的歌手的名字： ")
#     album = input("请输入该专辑: ")
#     if name == 'quit' or album == 'quit':
#         break;
#     test = make_album(name,album)
#     print(test)
def greet_users(names):
    for name in names:
        print(f"Hello {name}")
names = ['zhao yixu','zhu fengyuan','wang xinyu','xia danping']
greet_users(names)

messages = ['I love many people','I love you','I will study hard']
new_messages = []
def show_messages(messages):
    for message in messages:
        send_message(new_messages,message)
        print(message)
def send_message(messages,message):
    messages.append(message)
show_messages(messages)
print(new_messages)

#传递任意数量的实参 *toppings
def make_pizza(*toppings):
    print(toppings)
def make_pizza_pro(*toppings):
    for topping in toppings:
        print(topping)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
make_pizza_pro('pepperoni')
make_pizza_pro('mushroom','green peppers','extra cheese')

def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

#三明治
def make_sandwich(*toppings):
    toppings = ','.join(str(i) for i in toppings)
    print(f"该三明治所用到的食材是 {toppings}")
make_sandwich('mushroom','green peppers','extra cheese')