import math

print('请输入圆的半径：')
r = input()
r = int(r)


def area(r):
    return math.pi * r * r


def length(r):
    return math.pi * 2 * r


print('你输入的半径为：', r, '\n圆的面积为：', area(r), '\n圆的周长为：', length(r))
