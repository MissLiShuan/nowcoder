# -*- coding: utf-8 -*-
'''
题目描述
有两个用字符串表示的非常大的大整数,算出他们的乘积，也是用字符串表示。不能用系统自带的大整数类型。

输入描述:
空格分隔的两个字符串，代表输入的两个大整数

输出描述:
输入的乘积，用字符串表示

示例1

输入
72106547548473106236 982161082972751393

输出
70820244829634538040848656466105986748
'''
import sys

line=sys.stdin.readline()
line=line.strip().split()
line=line.strip().split()
array0=[]
array1=[]
summ=[]
for i in line[0]:
    array0.append(int(i))#该for循环用于遍历第一个字符串，将第一个字符串的字符逐个转换成整数型，并保存在array0列表中
for i in line[1]:
    array1.append(int(i))#该for循环用于遍历第二个字符串，将第二个字符串的字符逐个转换成整数型，并保存在array1列表中
if len(array0)>=len(array1):#如果第一个字符串的长度比较大，则将列表array1进行反转，
    sum0=int(line[0])#sum0用来保存line[0]的数值大小
    array1.reverse()#将列表array1进行反转，从而从个位开始与line[0]的数值大小想乘，最后将每位相乘的结果加起来
    for i in range(len(array1)):#该for循环遍历的是line[1]的个位，十位，百位...
        zero='0'*i#0的个数是位数的倍数
        num0=sum0*array1[i]
        num0=str(num0)+zero#将num0转换成字符串，然后和0的个数相连接
        summ.append(int(num0))#最后将每位相乘的结果转换成int，放到list中
else:#则将列表array0进行反转，步骤同上
    sum1 = int(line[1])
    array0.reverse()
    for i in range(len(array0)):
        zero = '0' * i
        num0 = sum1 * array0[i]
        num0 = str(num0) + zero
        summ.append(int(num0))
print(str(sum(summ)))#将list中每位相乘的结果加起来，并转换成字符串的形式即为结果
'''
笔记1：##############sys.stdin.readline( )和input()的区别######################
sys.stdin.readline()会将标准输入全部获取，包括末尾的'\n'
input()会把‘\n’忽略

import sys
a=sys.stdin.readline()
b=input()
print(len(a),len(b))

执行：
abc
abc
4 3

如果在平时使用sys.stdin.readline( )获取输入的话，不要忘了去掉末尾的换行符，
可以用strip( )函数去掉（sys.stdin.readline( ).strip('\n')），这样处理一下就行了

import sys
a=sys.stdin.readline().strip()
b=input()
print(len(a),len(b))

执行结果：
abc
abc
3 3

笔记2####################strip()的用法#######################################
描述：Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

语法：str.strip([chars]);

参数：chars -- 移除字符串头尾指定的字符序列。

返回值：返回移除字符串头尾指定的字符生成的新字符串。

实例

以下实例展示了strip()函数的使用方法：
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "00000003210Runoob01230000000"; 
print str.strip( '0' );  # 去除首尾字符 0  
str2 = "   Runoob      ";   # 去除首尾空格
print str2.strip();
以上实例输出结果如下：
3210Runoob0123
Runoob
从结果上看，可以注意到中间部分的字符并未删除。
以上下例演示了只要头尾包含有指定字符序列中的字符就删除：
实例
#!/usr/bin/python
# -*- coding: UTF-8 -*-
str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12
以上实例输出结果如下：
3abcrunoob3

笔记3##################split()方法的用法####################################
描述：split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

语法：str.split(str="", num=string.count(str)).

参数：str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    num -- 分割次数。默认为 -1, 即分隔所有。
    
返回值：返回分割后的字符串列表。

实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );       # 以空格为分隔符，包含 \n
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
以上实例输出结果如下：
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
以下实例以 # 号为分隔符，指定第二个参数为 1，返回两个参数列表。
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
txt = "Google#Runoob#Taobao#Facebook"
 
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
 
print x
以上实例输出结果如下：
['Google', 'Runoob#Taobao#Facebook']

笔记4#########################reverse() 函数####################################
描述:reverse() 函数用于反向列表中元素。
语法:list.reverse()
参数:NA。
返回值:该方法没有返回值，但是会对列表的元素进行反向排序。
实例
以下实例展示了 reverse()函数的使用方法：
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print "List : ", aList
以上实例输出结果如下：
List :  ['xyz', 'abc', 'zara', 'xyz', 123]
'''
