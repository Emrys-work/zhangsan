"""
print("hello world!")  # 字符串
print(2333)  # 整数
print(2.333)  # 小数
print(True)  # 布尔值 True False
print(())  # 元组
print([])  # 数组
print({})  # 字典

锄禾日当午
汗滴禾下土

print("哈哈",2333,2.333)
print("哈哈"+"嘻嘻")  # 字符串的拼接
print("哈哈哈"*100)
print(((1+2)*100-9.9)/2)
print(2<3)

# 变量
# 赋值
name = "张三"  # 把张三这个值赋值给了名字叫a的这个变量
print(name)

"""



# 数据格式的转换
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))


# a = float(input("请输入："))
# b = float(input("请输入："))
# print("input获取的内容：",a+b)


# a = "哈哈哈"
# print(len(a))

"""
练习：通过代码获取两段内容，并且计算他们的长度的和。
"""
# a = input("请输入：")
# b = input("请输入：")
# print("两段字符串的长度是：",len(a)+len(b))


# 元组,下标，从0开始编号
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1) 
# print(a[-2])
# 切片
# print(a[:4])  # 左闭右开
# print(a[4:9])
# print(a[9:])

# print(a.index("哈哈"))
# print(a.count("哈哈"))
# # 二维元组
# b = (a,"哈哈","嘻嘻")
# print(b[0][3])

# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# a.append("append1")
# a.append("append2")
# print(a)
# # 元组一定写好过后不可以修改，而数组是可以修改的
# a.insert(4,"insert")
# print(a)
# b = a.pop(0) # 剪切
# c = a.pop(0) # 剪切
# print(b+c)
# print(a)
# print(b)
# # a.clear()
# xx = ["你好","不好"]
# # a.extend(xx)
# print(a+xx)

# print(a)
# b = a.remove(1)
# print(b)
# print(a)

# # 下标不要超出范围 = 越界
# xx = [a,0,1,2,3]

"""
python的语法
所有的方法都是小括号结尾。比如，print(),input(),len()
元组、数组、字典的取值，都是用中括号,比如 a[0]
元组、数组、字典的定义，分别是(),[],{}
"""



"""
字典的特点
1、字典中的值没有顺序。
2、字典的结构必须是 键值对的结构。 key:value  
3、字典的取值，是通过key去取这个value
"""
a = {"name":"张三",0:"哈哈","age":25}
# 取值
print(a["name"])
# 新增
a["high"] = "183cm"
print(a)
# 修改
a["name"] = "李四"
print(a)
b = a.get("name")
print(b)
b = a.pop("name")
print(b)
print(a)
a.update(name="哈哈")
print(a)
print("----------------------")
print(a.get("name11"))
# print(a["name11"])

# 数组和字典的删除
del a["name"]
print(a)

del a[0]


"""
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括了，name,age,sex。
"""
