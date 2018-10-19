import math

"""
【战胜拖延症，组团学 Python】第三课：

1. 了解 Python 的基本数据结构和函数

2. 将第二课中的程序改写成函数的形式。任意编写一个 List 作为函数的参数，
    判断 List 中的每个元素是否为素数。并将是素数的元素打印为字典。（可以随意设置 key）
"""
def isPrime(numbers):
    results = {}
    if len(numbers) == 0:
        return 'list为空，没有需要判断的数字'
    else:
        for i in range(0, len(numbers)):
            results[numbers[i]] = True
            if numbers[i] <= 1:
                results[numbers[i]] = False
            else:
                for j in range(2, int(math.sqrt(numbers[i]))+1):
                    if numbers[i] % j == 0:
                        results[numbers[i]] = False

    return results


if __name__ == '__main__':
    numbers = [1, -1, -1, 3, 5, 4, 6, 9]
    print(isPrime(numbers))