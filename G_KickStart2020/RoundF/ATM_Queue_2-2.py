# FINALLY GOT 2 OF 2

import sys
import itertools
import math
import bisect

T = int(input())

dict = {}


for x in range(T):
    N, X = map(int, input().split())
    amounts = list(map(int, input().split()))
    order = []
    # forDeletion = []
    # deleted = 0


    # while len(peopleLeft) > 0:
    # print(len(forDeletion))

    for index, amount in enumerate(amounts):
        numberOfTimes = math.ceil(amount/X)
        bisect.insort_right(order, (numberOfTimes, index+1))

        # print(index, deleted)
        # if moneyLeft > 0:
        #     amounts[index] = moneyLeft
        # else:
        #     order.append(index+ 1)
        #     forDeletion.append(index)

        # deleted += len(forDeletion)
        # peopleLeft = np.delete(peopleLeft, forDeletion).tolist()
        # forDeletion = []

    orderValues = [i[1] for i in order]
    
    dict.update({x+1: orderValues})


for case, orderList in dict.items():
    print("Case #{}:".format(case) , *orderList)  
    sys.stdout.flush()

    #boboquack answer:
    # cases=int(input())
    # for case in range(1,cases+1):
    #     n,x=map(int,input().split())
    #     k=list(map(int,input().split()))
    #     l=[[(k[i]+x-1)//x,i+1] for i in range(n)]
    #     l.sort()
    #     print('Case #'+str(case)+':',*(i[1] for i in l))
