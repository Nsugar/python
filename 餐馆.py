class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"餐馆的名字是: {self.restaurant_name}")
        print(f"餐馆的菜品是： {self.cuisine_type}")
    def open_restaurant(self):
        print("餐馆正在营业")
    def set_number_served(self,count):
        self.number_served = count
        print(f"目前的就餐人数是 {count}")
    def increment_number_served(self,count):
        self.number_served += count

class Restaurant_0(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
r = Restaurant('二年级火锅店','酸汤火锅')
print(r.restaurant_name)
print(r.cuisine_type)
r.describe_restaurant()
r.open_restaurant()