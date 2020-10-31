# -*- coding: utf-8 -*-
# __author__ = 'Ayayaneru'

import os
import re

print('**************************************')
print('注意：本脚本会更改当前文件夹下所有文件！')
print('**************************************')
print('请输入修改后文件名称：')
topName = input()
old = []
new = []
for file in os.listdir():  # 当前文件夹内循环
    key_str = False
    episode = ''
    for str in file:  # 对单个文件的文件名逐个字符循环
        if str == '[' or str == '(':
            key_str = True
        if key_str == True:  # 提取文件名括号内的部分
            episode += str
        if str == ']' or str == ')':
            key_str = False
            if re.match(r'\d+',episode[1:-1]):  # 只保留第一个括号内为数字的部分
                try:
                    format = '.' + re.match(r'^(.+?)\.(.+)$',file).group(2)  # 文件格式
                except:
                    format = ''  # 文件夹或无格式文件
                newName = topName + episode + format
                print(file,'-->',newName)
                old.append(file)
                new.append(newName)
                break
            episode = ''
print('^ 按回车键后将做以上修改 ^')
input()
for O,N in zip(old,new):
    try:
        os.rename(O,N)  # 保留文件格式并重命名文件
    except:
        print(O,'-->',N,'失败！')
        print('请检查该文件名能否被修改 或文件重名了')
        input()
        exit()
    finally:
        print(O,'-->',N,'成功！')