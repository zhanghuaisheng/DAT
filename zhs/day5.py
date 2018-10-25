'''
【战胜拖延症，组团学 Python】第三课：
1. 了解 Python 的基本数据结构和函数
2. 将第二课中的程序改写成函数的形式。任意编写一个 List 作为函数的参数，判断 List 中的每个元素是否为素数。并将是素数的元素打印为字典。（可以随意设置 key）
'''
import math
def isPrime(l):
    
    dic={}
    if l == []:
        dic['l']='空list，无值'
    else:
        for i in range(0,len(l)-1):
            a = 0 #记录不是整除的次数
            if l[i] <= 1:
                dic[l[i]] = '不是素数'
            else:
                for j in range(2,l[i]):
                    if l[i] % j != 0:
                        a+=1
                if a == l[i]-2:
                    dic[l[i]] ='素数'
                else:
                    dic[l[i]] ='非素数'
    return dic

if __name__ == '__main__':
    num = [1,2,3,4,5,6,7,8,9,10,-1,-2]
    num2 = []
    print(isPrime(num))
    print(isPrime(num2))
    