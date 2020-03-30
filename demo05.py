"""
import requests


url = "http://openapi.tuling123.com/openapi/api/v2"
data = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "0f20cf149ea84196965c797eeecaa9e4",
        "userId": ""
    }
}
res = requests.post(url,json=data)
print(res.json())

"""

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

cookies = [{'domain': '.bilibili.com', 'expiry': 1600872163.470666, 'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': 'f61f45c61e3839e89434b2d0713fde87'}, {'domain': '.bilibili.com', 'expiry': 1600872163.470655, 'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': '866c49e0%2C1600873163%2C69749*31'}, {'domain': '.bilibili.com', 'expiry': 1600872163.470612, 'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '6770138'}, {'domain': '.bilibili.com', 'expiry': 1616857150.037282, 'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': 'cm6wpqig'}, 
{'domain': '.bilibili.com', 'expiry': 1679929147.426912, 'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': '6F09AE83-85A2-4549-B83C-6DABE7001A0C155818infoc'}, {'domain': '.bilibili.com', 'expiry': 1600872163.470644, 'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '7545e579c70171ea'}, {'domain': '.bilibili.com', 'expiry': 1616857147, 'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '21799BF1-9F72-0B9D-D8FD-F7875B9A466247156infoc'}, {'domain': '.bilibili.com', 'httpOnly': False, 'name': 'INTVER', 'path': '/', 'secure': False, 'value': '1'}] 

driver.get("https://www.bilibili.com/")
driver.delete_all_cookies()
for c in cookies:
    if c.get("expiry") != None:
        del c["expiry"]
    driver.add_cookie(c)
driver.refresh()
time.sleep(20)
driver.quit()



