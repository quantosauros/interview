'''
Created on 2015. 5. 19.

@author: Jay
http://www.algoqueue.com/algoqueue/default/view/3866624/find-2nd-largest-number-in-an-array-with-minimum-comparisons
'''

def procedure(A):
    length = len(A)
    odd = False
    arraySize = length / 2
    if length % 2 == 1:
        odd = True
        length = length - 1
        arraySize = length / 2 + 1
    index = 0

    C = range(arraySize)
    B = range(arraySize)   
     
    for i in range(0, length, 2):        
        if A[i] > A[i+1]:                   
            B[index] = A[i]
            C[index] = A[i+1]          
        else :
            B[index] = A[i+1]
            C[index] = A[i]            
        index = index + 1
    
    if odd:
        B[index] = A[length]
        C[index] = -1

    return (B,C)

A = (45,44,711,8,15,2,614141,35555554,1,151,125,11)
#A = [[5],[4],[1],[8],[7],[2],[6],[3]]
length = len(A)
C = []
B = []
print(A) 
index = 0
while length > 1:
    print("=====================")        
    #[A,tmpC] = procedure(A)
    (A,tmpC) = procedure(A)
    C.append(tmpC)
    B.append(A)  
    print(A)
    print(B)
    print(C)
    length = len(A)

print("The Largest value: " + str(A[0]))

goal = C[len(B) - 1][0]
largestValue = A[0]
for i in range(0,len(C)):
    arr1 = B[i]
    arr2 = C[i]
    for j in range(0, len(arr1)):
        #print(i,j)
        if (arr1[j] == largestValue):
            if (arr2[j] > goal):
                print("changed : " + str(goal) + " -> " + str(arr2[j]))
                goal = arr2[j]
              
print("Second Largest value: " + str(goal))
    