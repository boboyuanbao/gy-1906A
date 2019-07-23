# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
#
#
# '''
# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# '''
# #def 定义方法的关键字，juge_3_2是方法名 为自定义变量，自定义变量不可以以数字开头，()参数列表：
# def juge_3_2(a):
#
#     # 第一步：统一符号  对字符串的处理，用replace（）
#     #input 输入方法，()变量值
#
#     a = a.replace("''",'"')
#     #print(a)
#
#     # 第二步：去掉中括号 字符串截取  [::]
#     a = a[2:-2]
#     #print(a)
#     # 第三步：变成list  字符串切片  .split（） 新建一个list变量
#     a_li = a.split('" , "')
#     #print(a_li)
#     # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
#     b = {}
#     for i in a_li:
#         i_k = i[1:]
#         #print(i_k )
#     # 第五步：统计相同的数字个数  用字典去统计
#         if(i_k in b):
#             b[i_k] += 1
#         else:
#             b[i_k] =1
#         #print(b)
#     # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
#     v1=0 #如果key对应的值为3 则v1 =1,否则为0
#     v2=0 #如果key对应的值为2 则v2=1,否则为0
#     for ky in b:
#         if( b[ky] == 3):
#             v1 = 1
#         if(b[ky] == 2):
#             v2 = 1
#     if(v1 == 1 and v2 == 1):
#         print('可以三带二')
#     else:
#         print('不可以三带二')
# #open python 提供的一个内置函数：作用就是打开一个文件，参数一：文件路径，参数二：文件的打开模式r只读，W可写入，a可读可写入
# #with open()as f 类似于f = open (),它可以在with的代码执行出问题的时候，做一些资源释放的工作
#
# with open ("D:\\softwaradata1\\pycharm\\hxj.day1\\hxj\\day04\\cards.txt",'r') as f:
#     lin = f.readlines()
#     for line in lin :
#         line = line.replace('\ n',"")
#         print(line)
#         juge_3_2(line)


# #计算出两个数的加减乘除
# def sum (numb1,numb2):
#        print(numb1 + numb2)
#         # print(numb1 - numb1)
#         # print(numb1 * numb1)
#         # print(numb1 / numb1)
#
# with open("D:\\softwaradata1\\pycharm\\hxj.day1\\hxj\\day04\\numb.txt") as f:
#     f_li = f.readlines()
#     for line in f_li:
#         line = line.replace('/n',"")
#         line_li = line.split(",")
#         sum(int(line_li[0]),int(line_li[1]))
#         print(line)
#
# def sum (a,b):
#     s = a + b
#     print(a,'+',b, '=',s)
#     return s
#
# def sum1 (c,d):
#     s1 = c - d
#     print (c,'-',d,'=',s1)
#
#
# def sum2 (a,b):
#     s2 = a * b
#     print (a,'*',b,'=',s2)
#
#
# def sum3 (a,b):
#     if (b != 0):
#         s3 = a / b
#         print (a,'/',b,'=',s3)
#     else:
#         ('除数不能为0')
#
# sum(34,23,43)
# # sum(sum(34,23),43)
#
# def bo():
#     return '波波是只猫'
# print(bo())
#
# def bo(nu1,nu2,nu3):
#     return '{}是{}{}'.format(nu1,nu2,nu3)
# print(bo('波波','只','猫'))
#
# def bo(nu1,nu2,nu3):
#     return'{u1}是{u2}{u3}'.format(u3=nu3,u2=nu2,u1=nu1)
# # print(bo('波波','只','猫'))
#
# def buy_coffee(numb1,numb2):
#     print("来到咖啡店")
#     cup_nu = numb1
#     print("告诉营业员我要买",cup_nu,"杯")
#     kafei_price = 30
#     money = numb2
#     print("给钱",money)
#     change_money = money - kafei_price*cup_nu
#     print("拿走",cup_nu,"杯咖啡，还剩",change_money,"元钱")
#
# with open("E:\\softwaredata\\python\\gy-1906A\\demo\\day04\\caffee_data") as f:
#     f_li= f.readlines()
#     for line in f_li:
#         line = line.replace("\n","")
#         line_li = line.split(",")
#         buy_coffee(int(line_li[0]), int(line_li[1]))
# #  int()  把字符串转为数字类型
#  str()
        # print(line)
# buy_coffee(15,500)

def buy_coffee (cash=100,cups=1):
    #去咖啡店
    print("去咖啡店")
    #告诉服务员要几杯咖啡
    cup_num = cups
    print("告诉服务员要",cup_num,"杯咖啡")
    #服务员告诉你要多少钱
    print("服务员告诉你要",cup_num*30,"钱")
    #你给服务员多少钱
    money = cash
    print("你给服务员",money,"钱")
    #服务员找零，给你咖啡
    print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
buy_coffee()


