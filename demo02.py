# 判断  缩进，

# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("你应该退休了")
# elif age > 30:
#     print("家庭的责任很重吧")
# elif age > 20:
#     print("一定要好好规划你的未来！")
# else:
#     print("读书的时候，要认真！")

# if age > 20 and age <=30:
#     print("22222222")
# elif age > 30:
#     print("333333333")
# elif age > 60:
#     print("66666666")
# else:
#     print("xxxxxxxxxx") 


# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")

# a = "dkjfedj"
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")


# a = 1
# while a < 10:
#     print("哈哈哈啊哈",a)
#     a = a + 2



# 遍历

# a = "你好，今天你吃了吗？"
# a = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in a:
#     print(i)

# for i in range(1,10):
#     for j in range(1,i+1):
#         if i == 3:
#             continue
#         print(i,"X",j,"=",i*j,end="  ")
#     print()


# for i in range(10):
#     if i == 3:
#         break
#     print("哈哈哈")





# def 方法的声明
# checkname 方法的名字
# username 方法的参数
# """方法的说明"""
# 方法的逻辑代码





"""
返回值，返回后我们可以对这个值做其他的操作
而，print不能
"""




# username = input("请输入你的账号：")
# password = input("请输入你的密码：")
# if checkname(username) == True:
#     if len(password) >= 8 and len(password) <= 12:
#         print("注册成功！",{username:password})
#     else:
#         print("密码必须8-12位！")
# else:
#     print(checkname(username))


def jiafa(a,b):
    """
    这个方法的作用是实现两个数字相加
    """
    if type(a) is int and type(b) is int:
        print(a+b)
    else:
        return "输入的数据类型不正确"





