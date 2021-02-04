# @Time : 2021/1/18 15:15 
# @Author : 帅气的亮亮
# @File : function.py 
# @Software: PyCharm
# @Notes: 良好的代码除了逻辑还有注释

"""
函数到装饰器
4个核心概念
1. 函数可以赋予变量
2. 函数可以当作函数的参数
3. 函数嵌套函数
4. 闭包(函数作为函数返回值)
"""


# 1.作为变量
def func(message):
    print("Show a message:{}".format(message))


show_message = func
show_message("1.function advanced")


# 2.参数
def get_message(message):
    return "Show a message :"+message


def root_call(func, message):
    print(func(message))


root_call(get_message, "2.function advanced")


# 3.嵌套
def func(message):
    def get_message(message):
        print("Show a message :{}".format(message))
    return get_message(message)


func("3.function advanced")


# 4.作为返回值
def func_closure():
    def get_message(message):
        print("Show a message:{}".format(message))
    return get_message


send_message = func_closure()
send_message("4.function advanced")
print("++"*30)


def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()
    return wrapper


def greet():
    print("Decorator wrapper")


greet = my_decorator(greet)
greet()

print("=@="*20)


# 语法糖@
@my_decorator
def greet():
    print("Decorator @:wrapper")


greet()

print("--"*30)


# 带参数的装饰器
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print("wrapper of decorator:@param{}".format(i))
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)


greet("decorator")

print("=="*30)
print(greet.__name__)

help(greet)
print("=*="*15)

print("类装饰器")


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("num of calls is :{}".format(self.num_calls))


@Count
def example():
    print("hello decorator")


example()


