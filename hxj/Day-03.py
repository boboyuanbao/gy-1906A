# # find
# # a = 'https://turbo.net/browsers'
# # xy=a.split('://')[0]
# # xy1=a.split('://')[1]
# # print(xy)
# # print(xy1)
# # ym=xy1[:xy1.find('/')]
# # print(ym)
# #
# # uri=xy1[xy1.find('/'):]
# # print(uri)
# #①增
# #逐个增加单个元素
# a=[]
# a.append(1)
# a.append(2)
# print(a)
# b=['波波猫','元宝狗']
# #两表合成一个表（两种方法）
# print(a+b)
#
# a.extend(b)
# print(a)
# #②删 单个元素，pop(下标对应的元素)
# a.pop(1)
# print(a)
# #清空列表（两种方法)
# a=[]
# print(a)
#
# a.clear()
# print(a)
#
# #③改某个元素的值
# #单个改
# a[1] = 0
# print(a)
# #多个改（和单个改原理一样）
# a[1],a[2],a[3]=4,5,6
# print(a)
#
# #④查
# #根据下标进行单个查询
# print(a[0])
# #遍历（把数组中的数据逐个拿出来）需借助循环
# for i in a :
#     print(i)
# #查看字符串长度
# print(len(a))

#⑤截取
#截取部分数据
# print(a[1:3])
# #倒序
# print(a[::-1])
# #隔一个截取一个
# print(a[::2])
# #成员判断（列表中是否存在某个数据）
# if(5 in a):
#     print('存在列表中')
# else:
#     print('不存在列表中')

#字典增
#字典的特性：字典中的key是唯一的不允许同一个键出现两次，创建时一个值被赋予两次，只会记住最后一个值
#key是不可以改变，数字加 字符串 元组，元组(1,2,3，4)可以作为key，但（1,[3]）不可以
#新增一组数据
a={}
a['猫']='bobo'
print(a)
#删
#删除某一对值，pop参数只能为key
#a.pop('姓名')
#改
a['猫']='波妞'
print(a)

#合并
a = {'姓名':'波波'}
b = {'年龄':'1'}
a.update(b)
print(a)
#第二种合并，会生成一个新的字典
print(dict(a,**b))
