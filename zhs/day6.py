

'''
【战胜拖延症，组团学 Python】第四课：
1. 掌握链接中 Python 教程的高级特性
2. 利用生成器生成斐波那契数列
'''
def fibonacci(num):
    a = 0
    b = 1
    i = 0
    while i < num:
        yield b
        a,b = b, a+b
        i +=1
    

if __name__ == '__main__':
    flag = True
    while flag:
        num = int(input("斐波那契数列位数："))
        if num == -1 :
            flag = False
        else:
            print( [ i for i in fibonacci(num)])
    