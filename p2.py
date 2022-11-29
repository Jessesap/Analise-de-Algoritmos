import time
start = time.time()
import numpy as np
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = np.random.randint(10,101,size=10000)
bubbleSort(alist)
print(alist)
end = time.time()
print("\nTempo de execução :", end-start)
