'''
ProjectEuler - Problem 2

Even Fibonacci numbers
========================
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

@author: Manuel Guillen
'''
import math

if __name__ == '__main__':
    '''
    Fibonacci Sequence:            a_n = a_{n-1} + a_{n-2}, a_1 = a_2 = 1
    Solves to explicit formula:    a_n = 1/sqrt(5) * (phi^n - psi^n)        phi = (1+sqrt(5))/2, psi = (1-sqrt(5))/2
    
    Since |psi| < 3/4              a_n = round(phi^n / sqrt(5))  ,  for n >= 3
    
    Since the Fibonacci sequence goes odd, odd, even, odd, odd, even, ..., the even terms are a_3, a_6, ...
    
    So the n^th even Fibonacci term is b_n = a_{3n} = round(phi^{3n} / sqrt(5)) = round((2+sqrt(5))^n / sqrt(5))
    '''
    
    sqrt5 = math.sqrt(5)
    base1 = 2+sqrt5
    
    sum = 0
    n = 0
    num = 0
    while (num < 4000000):
        sum += num
        n += 1
        num = int(0.5+(math.pow(base1,n)/sqrt5))
    
    print(sum)