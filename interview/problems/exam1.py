'''
Created on 2015. 5. 21.

@author: Jay
'''
#===============================================================================
# 
# A = 167
# B = 91
# C = 0
# 
# while A-2 > B :
#     A = A - 2
#     C = C + 1
#     
# print(C)
#===============================================================================

A = 1.0
B = 100.0
C = 0

for i in range(1, 10001):
    C = (A+B)/2.0
    print("A :" + str(A))
    print("B :" + str(B))
    print("C :" + str(C))
    if A == C or B == C:
        break;
    A = B
    B = C
    
    

print(C)
