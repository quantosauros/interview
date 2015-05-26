'''
Created on 2015. 5. 20.

@author: Jay
http://discuss.fogcreek.com/techInterview/default.asp?cmd=show&ixPost=1921
'''
import random

def grandmaProblem(simNum):
    
    ownSeat = 0    
    for i in range(0, simNum):        
        seat = [False] * 100
        seatNum = int(random.random()*100)
        seat[seatNum] = True
        
        for j in range(1, 99):            
            if not seat[j]:
                seat[j] = True
            else:
                seatNum = int(random.random()*100)           
                while seat[seatNum]:                    
                    seatNum = int(random.random()*100)
                seat[seatNum] = True
                            
            #print(str(rnd[j]) + " , " + str(j))
            
        if seat[99] == False:
            ownSeat = ownSeat + 1
            
    return ownSeat

a = grandmaProblem(10000)

print(a)
    
