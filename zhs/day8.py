import math
import time
def showTime(func):
    def wrapper(*arg,**kw):
        showtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print(showtime)
        return func(*arg,**kw)
    return wrapper
@ showTime
def isPrime(l): 
    time.sleep(2)
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
    