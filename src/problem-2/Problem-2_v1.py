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
    a1 = 1
    a2 = 1
    a3 = 2
    
    sum = 0
    while(a3 < 4000000):
        if a3 % 2 == 0:
            sum += a3
        a1 = a2
        a2 = a3
        a3 = a1 + a2
    
    print(sum)