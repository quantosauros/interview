'''
Created on 2015. 5. 20.

@author: Jay
'''

def F(x):
    return x * x

def integrateF(a, b, N):
    result = 0
    length = (b-a)/N
    
    for i in range(0,N):
        result = result + F(a + (0.5 + i)*length)
    
    result = result * length
    
    return result

def trapeziumRule(a, b, N):
    result = 0
    length = (b-a)/N
    
    result = F(a) + F(b)
    for i in range(1,N):
        result = result + 2 * F(a + i * length)

    result = result * length / 2
    
    return result

y = integrateF(1.0, 2.0, 1000)
trapezium = trapeziumRule(1.0, 2.0, 1000)

print(y)
print(trapezium)
print(float(7.0/3.0))