# -*- coding: utf-8 -*-
'''
【战胜拖延症，组团学 Python】第一课：
1. 掌握 Python 变量，输入输出，+-*/%运算
2. 编写 Python 程序，此程序可以从命令行接收一个数字输入，并输出以该数字为半径的圆的周长和面积。
'''
import math

if __name__ == '__main__':
    #task1
    n1 = input("请输入第一个数字： ")
    n2 = input("请输入第二个数字： ")
    
    sum_number = float(n1)+float(n2)# 加法+
    minus = float(n1)-float(n2) #减法 -
    mul = float(n1) * float(n2)  #乘法 *
    #除法 /
    if float(n2) == 0:
        print('除数为0，无法整除')
    else :
        div = float(n1) / float(n2)
        print("除法运算：" + n1 + '/' + n2 + ' = ' +str(div))
    mod = int(n1) % int(n2) #取余 %
    print("加法运算：" + n1 + ' + ' + n2 + ' = ' + str(sum_number))
    print("减法运算：" + n1 + ' - ' + n2 + ' = ' + str(minus))
    print("乘法运算：" + n1 + ' * ' + n2 + ' = ' + str(mul))
    print("取余运算：" + n1 + ' % ' + n2 + ' = ' + str(mod))

    #task2
    radius = (input('请输入半径： '))  
    cricle_l = 2*math.pi*float(radius)      #圆周长
    cricle_s = math.pi*(float(radius))**2   #圆面积
    print('半径为%s的圆周长为：' %radius + str(cricle_l))
    print('半径为%s的圆面积为：' %radius + str(cricle_l))

    