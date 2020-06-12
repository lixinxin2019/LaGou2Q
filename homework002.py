# 课后作业：自己写一个面向对象的例子
# 描述：
# 创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
import yaml


class Animal:

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print(f"{self.name} 会叫")

    def run(self):
        print(f"{self.name} 会跑")


# 创建子类【猫】，继承【动物类】，
class Cat(Animal):
    # - 复写父类的__init__方法，继承父类的属性，
    # - 添加一个新的属性，毛发=短毛，
    def __init__(self, name, color, age, gender, hair="短毛"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    # - 添加一个新的方法， 会捉老鼠，
    def catch_mouse(self):
        print(f"{self.name} 会捉老鼠")

    # - 复写父类的‘【会叫】的方法，改成【喵喵叫】
    def shout(self):
        print(f"{self.name} 会喵喵叫~")

    # 打印猫猫的信息
    def info(self):
        print(f"猫猫的名字是：{self.name},颜色是：{self.color},年龄是：{self.age},性别是：{self.gender},毛发是：{self.hair},捉到了老鼠")


# 创建子类【狗】，继承【动物类】，
class Dog(Animal):
    # - 复写父类的__init__方法，继承父类的属性，
    # - 添加一个新的属性，毛发=长毛，
    def __init__(self, name, color, age, gender, hair="长毛"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    # - 添加一个新的方法， 会看家，
    def outstanding(self):
        print(f"{self.name} 会看家！")

    # - 复写父类的【会叫】的方法，改成【汪汪叫】
    def shout(self):
        print(f"{self.name} 会汪汪叫！")

    # - 打印狗狗的信息
    def info(self):
        print(f"狗狗的名字是：{self.name},颜色是：{self.color},年龄是：{self.age},性别是：{self.gender},毛发是：{self.hair}")


if __name__ == '__main__':
    #调用data.yaml中的数据：
    with open("data.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
    mycat = datas["mycat"]
    mydog = datas["mydog"]

    # 创建一个猫猫实例
    #cat = Cat("小黑猫", "黑色", 1, "母猫")

    #创建一个猫猫实例，使用data.yaml中的数据管理实例的属性
    cat = Cat(mycat["name"], mycat["color"], mycat["age"], mycat["gender"])

    # - 调用捉老鼠的方法
    cat.catch_mouse()

    # - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
    cat.info()

    #===========================================================
    # 创建一个狗狗实例
    #dog = Dog("阿黄", "黄色", 1, "母狗")

    # 创建一个狗狗实例，使用data.yaml中的数据管理实例的属性
    dog = Dog(mydog["name"], mydog["color"], mydog["age"], mydog["gender"])

    # - 调用【会看家】的方法
    dog.outstanding()

    # - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
    dog.info()

    # 4、使用 yaml 来管理实例的属性
    # 5、提交代码到自己的github仓库， 贴到作业贴上
