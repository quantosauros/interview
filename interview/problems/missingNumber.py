'''
Created on 2015. 5. 20.

@author: Jay
'''

def findMissingInt(numbers):
    N = len(numbers) + 1
    total = N * (N + 1)/2
    x = 0
    
    for i in range(0,N-1):
        x = x + numbers[i]
    
    r = total - x
    return r;


number = (1,2,3,4,5,6,7,8,9,11)

aa = findMissingInt(number)

print(aa)
    