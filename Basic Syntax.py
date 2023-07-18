name = "zhiting chen"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "Zhiting"
last_name = "Chen"
print(f"{first_name} {last_name}") 
#Similar to strcat in C, f is format for short

#strip the white space
best_language = '  Python  '
test_lspace = 'Which is the best language?'
test_rspace = '!'
print(f"{test_lspace}{best_language}{test_rspace}")
print(f"{test_lspace}{best_language.rstrip()}{test_rspace}")
print(f"{test_lspace}{best_language.lstrip()}{test_rspace}")
print(f"{test_lspace}{best_language.strip()}{test_rspace}")

url = "http://hello.com"
print(url.removeprefix('http://'))

#采用下划线来表示较大数字
universe_age = 14_000_000_000
print(universe_age)

#多变量命名
x,y,z = 0,0,0

#全大写表示常量
MAX = 1000

#缩进是重要的
magicians = ['A', 'B', 'C']
for magician in magicians:
    print(magician)

# list comprehension 列表推导式
squares = [value**2 for value in range(1, 11)]
print(squares)

#Slice 切片：使用数组中的某些元素
list_1 = ['a', 'b', 'c']
print(list_1[0:3:2])# 获取1，2，3；第三个成员表示步长

# 复制列表元素
list_2 = list_1[:]
print(list_2)

#Dictionary 字典---键值对key&value
user_0 = {
    'name':'Jay',# Remember the comma
    'first':'enrico',
    'last':'fermi',
}
for name, first in user_0.items():
    print(f"\nkey:{name}")
    print(f"value:{first}")
# Only output the keys
for key in user_0.keys():
    print(key)
# Only output the values
for value in user_0.values():
    print(value)
for value in set(user_0.values()): #使用set集合去重
    print(value)

# 列表中嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# 字典中嵌套列表
favorite_languages = {
    'jay':['python', 'C'],
    'sarah':['C'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()} favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#使用用户输入
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")#结合printf与scanf
    response = input("Which mountain do you climb today? ")

    responses[name] = response #Remember this syntax
    repeat = input("More person?(yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Result---")
for name, response in responses.items():
    print(f"{name} climb {response}.") #{}is important


# Function
def describe_pet(pet_name, animal_type = 'dog'): # 描述形参
    """显示信息"""#docstring
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'edward')


def make_pizza(size, *toppings): #*表示任意数量的参数
    print(f"making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info): # **表示创建字典
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
# 可以传入任意多键值对
user_profile = build_profile('albert','einstein', location = 'princeton', field = 'physics')
print(user_profile)
    

# 导入模块及函数
from function import make_car as mc
# from ... import... 显式表示，不需要点号(function.make_car(...))
# from module_name import *  ---导入所有函数
car = mc('subaru', 'outback', color = 'blue', tow_package = True)
print(car)


# oop(object-oriented programming)
# 类 class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}, the cuisine type is {self.cuisine}")
    
    def open_restaurant(self):
        print("opening")

restaurant = Restaurant('Starbucks', 'coffee')
restaurant.describe_restaurant()
restaurant.open_restaurant()



        