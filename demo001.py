#a = "aaaaa"
#b = f"bbbbb{a}"
#c = "ccc"
#d = "ddd{}{}"
#print(a+b)#通过+将字符串a和b连接在一起
#print("abc" "def")#通过空格将两个字符串连接在一起
#print(b)
#print(d.format(a,c))

# List_e = [1,0.5,"a"]
# print(List_e[0])
# print(List_e[1])
# print(List_e[-1]) #-1代表倒数第一个
# print(List_e[0:3])#[0:3]是左开右闭[0,3)，代表取第1-3个


# a = 3
# if a == 0 :
#     print("a=0")
# elif a == 1:
#     print("a=1")
# elif a == 2:
#     print("a=2")
# else:
#     print("a不在合理输入范围内")

# 分段函数求值：
#         3x - 5 (x > 1)
# f(x) =  x + 2 ( -1 < x < 1)
#         5x + 3 ( x < -1)

x = -2
if x > 1:
    y = 3*x - 5
elif -1<= x <= 1:
    y = x + 2
elif x < -1:
    y = 5*x + 3
print(y)


