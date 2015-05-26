'''
Created on 2015. 5. 20.

@author: Jay
'''


def fibbonacci(n):
        
    f1 = 0
    f2 = 1
    for i in range(1, n):
        next = f1 + f2
        f1 = f2
        f2 = next
        print(f2)

    return f2

aa = fibbonacci(10)

print(aa)