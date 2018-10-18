import math
'''
    从命令台接收一个数字，判断其是不是素数。
    素数：在大于1的自然数中，除了1和它本身以外，不再有其它的因素。
'''


def isPrime(number):
    if number == 1:
        return '不是'
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return '不是'
    return '是'


if __name__ == '__main__':
    print('请输入一个整数:')
    number = int(input())
    flag = 'Y'
    while flag == 'y' or flag == 'Y':
        print('你输入的', number, isPrime(number), '素数')
        print('是否继续进行判断：y/n')
        flag = input().strip()
        if flag == 'y' or flag == 'Y':
            print('请输入一个整数:')
            number = int(input())
    print('你终止了判断，程序结束...')

