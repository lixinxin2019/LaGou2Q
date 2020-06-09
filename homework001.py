def func1():
    print("这是没有参数、没有返回值的方法")
def func2(a, b):
    print("这是有参数、有返回值的方法")
    c = a+b
    print(f"{a}+{b} = {c}")
    return c

if __name__ == '__main__':
    print(func1())
    print(func2(1,2))



