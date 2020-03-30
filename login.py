from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
cookies = [{'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'KLBRSID', 'path': '/', 'secure': False, 'value': '57358d62405ef24305120316801fd92a|1585323000|1585322985'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'secure': False, 'value': '1585323001'}, {'domain': '.zhihu.com', 'expiry': 1587914999.36036, 'httpOnly': True, 'name': 'z_c0', 'path': '/', 'secure': False, 'value': '"2|1:0|10:1585322997|4:z_c0|92:Mi4xZGF3a0FBQUFBQUFBZ0pwSjdqb0hFU2NBQUFDRUFsVk45YWlsWGdDYTFFN2lWQ3RqSnF1S0laOWdBejdydUFFdmpn|6722c613277739e077dbd190a12abd52500444d9c3ff4304b46e3bbb13dd5489"'}, {'domain': '.zhihu.com', 'expiry': 1616859000, 'httpOnly': False, 'name': 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'secure': False, 'value': '1585322988'}, {'domain': '.zhihu.com', 'expiry': 1679930987.933641, 'httpOnly': False, 'name': 'd_c0', 'path': '/', 'secure': False, 'value': '"AICaSe46BxGPTr7-2tUQwRLwSwdLctSTBp0=|1585322986"'}, {'domain': '.zhihu.com', 'expiry': 1585323047, 'httpOnly': False, 'name': '_gat_gtag_UA_149949619_1', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.zhihu.com', 'expiry': 1648395000, 'httpOnly': False, 'name': '_ga', 'path': 
'/', 'secure': False, 'value': 'GA1.2.627947956.1585322988'}, {'domain': '.zhihu.com', 'expiry': 1587914988.031025, 'httpOnly': True, 'name': 'capsion_ticket', 'path': '/', 'secure': False, 'value': '"2|1:0|10:1585322986|14:capsion_ticket|44:MWQzMWJjM2I3Y2U3NDE3ZGE0MGYzNDZiOGVkYmU0MjE=|1dbcb71bd65a809595be990db0f58947ff3d3e586592f304e930ffebff8d9f7a"'}, {'domain': '.zhihu.com', 'expiry': 1585409400, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1746775208.1585322988'}, {'domain': '.zhihu.com', 'expiry': 
1587915000, 'httpOnly': False, 'name': 'tst', 'path': '/', 'secure': False, 'value': 'r'}, {'domain': '.zhihu.com', 'expiry': 1663082987.040927, 'httpOnly': False, 'name': '_xsrf', 'path': '/', 'secure': False, 'value': 'yRScKwurcTxXm2Dd3KMNgehPAlf69R7Z'}, {'domain': '.zhihu.com', 'expiry': 1648394987.040848, 'httpOnly': False, 'name': '_zap', 'path': '/', 'secure': False, 'value': '91b65653-2a91-4149-b625-119135f1554d'}]
driver.get("http://www.zhihu.com")
driver.delete_all_cookies()
for c in cookies:
    if c.get("expiry") != None:
        del c["expiry"]
    driver.add_cookie(c)
driver.refresh()
time.sleep(20)
driver.quit()