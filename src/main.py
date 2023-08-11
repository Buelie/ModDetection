import os
import time
# 导入必须库OS & TIME

os.system('title ModDetection')
# 设置标题

if os.path.exists('mods') != True:
    print('没有mods文件夹,请确保软件在Minecraft版本文件夹内')
    time.sleep(3.5)
# 检测版本下是否存在mod文件夹

ModList = os.listdir('mods')
ModLen = len(ModList)
# 获取mod列表

if os.path.isfile("ModsList.txt") == True:
    os.remove('ModsList.txt')
# 检测是否有旧的输出文件

if os.path.isfile("ModsListConfig.txt") == False:
    with open("ModsListConfig.txt",'w',encoding='utf-8') as f:
        f.write('li')
        f.close()
# 创建配置文件,默认配置为 'li'

if open("ModsListConfig.txt",'r').read() == 'li':
    GetAS = ['<li>','</li>']
elif open("ModsListConfig.txt",'r').read() == 'air':
    GetAS = ['','']
elif open("ModsListConfig.txt",'r').read() == '*':
    GetAS = ['* **','**']
# 读取配置

if os.path.isfile("ModsList.txt") == False:
    with open("ModsList.txt",'w',encoding='utf-8') as f:
        f.write('')
        f.close()
# 生成输出文件

i = 0
while i <= ModLen:
    if ModList[i].endswith('.jar') == True:
        with open("ModsList.txt",'a',encoding='utf-8') as f:
            f.write(f'{GetAS[0]}{ModList[i]}{GetAS[1]}\n')
            f.close() 
        i += 1
    else:
        i += 1
# 打印到输出文件
