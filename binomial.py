import math

#@author Thinh 17021046

def factorial(n):
    """
    Tính giai thừa của n
    """
    if n <= 1:
        return 1;
    else:
        return n * factorial(n - 1);

def combination(i, p):
    """
    Tính C(i, n)
    """
    return factorial(p) / (factorial(i) * factorial(p - i));

def prob(n, p, q):
    return combination(n, q) * (p ** n) * (1 - p) ** (q - n);

def infoMeasure(n, p, q):
    return -math.log(prob(n, p, q), 2);

def sumP(n, p):
    """
    Tính tổng của xác suất của các symbol n của nguồn thông tin binomial
    n chạy từ 1 đến N
    """
    sum = 0 ;
    for i in range(1, n + 1):
        sum += prob(i, p, n);

    return sum;

def approxEntropy(n, p):
    """
    Tính entropy của phân bố binomial
    """
    sumHx = 0;
    for i in range(1, n + 1):
        sumHx += prob(i, p, n) * infoMeasure(i, p, n);
    return sumHx;

print(approxEntropy(3, 0.5));