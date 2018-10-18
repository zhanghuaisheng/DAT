'''
【战胜拖延症，组团学 Python】第二课
1. 掌握 Python 的 if-else 分支结构以及 while for 循环（包括 continue 和 break)
2. 编写一个程序，该程序可以从命令行接收一个数字输入并判断该数字是否为素数。
'''

if __name__ == '__main__':
    num = int(input('请输入一个大于1的整数： '))
    a = 0 #记录不是整除的次数
    if num <= 1:
        print('请输入一个大于1的整数')
    else:
        for i in range(2,num):
            if num % i != 0:
                a+=1
        if a == num-2:
            print('%d是一个素数' % num)
        else:
            print('%d不是一个素数' % num)
