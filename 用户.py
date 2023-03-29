class User:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name =last_name
        self.age = age
    def describe_user(self):
        print(f"\n用户的名字是 {self.first_name}{self.last_name}")
        print(f"用户的年龄是 {self.age}")
    def greet_user(self):
        print("今天又是元气满满的一天")
user_01 = User('zhao','yixu',20)
user_02 = User('zhu','fengyuan',20)
user_01 .describe_user()
user_02.describe_user()
user_01.greet_user()