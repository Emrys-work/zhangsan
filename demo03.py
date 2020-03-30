
"""
class 声明类的名字
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，叫self
"""

class GirlFriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age
    
    def caiyi(self,num):
        """
        才艺表演
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的才艺表演之：")
        if num == 1:
            print("胸口碎大石！")
        elif num == 2:
            print("唱跳RAP篮球")
        else:
            print("单手开瓶盖！")
    
    def chuyi(self):
        """
        厨艺持家
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的厨艺表演之：")
        print("精通八大菜系！中外融合！啥都会做！")


    def work(self):
        """
        工作挣钱
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的工作之：")
        print("开挖掘机！")
    



class Car():
    def __init__(self,pinpai,yanse,neishi,jilun):
        self.pinpai = pinpai
        self.yanse = yanse
        self.neishi = neishi
        self.jilun = jilun
    
    def bianxing(self):
        print("车子变身金刚喜羊羊！")
    
    def fly(self):
        print("车子开始起飞！")



class Nvpengy(GirlFriend):
    def work(self):
        print("修电脑")


zhangsan = Nvpengy("女","172","120","短发","25")
zhangsan.work()
zhangsan.chuyi()




