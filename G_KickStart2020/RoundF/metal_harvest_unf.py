
import sys
import itertools
import math
import bisect

T = int(input())

dict = {}


for x in range(T):
    N, K = map(int, input().split())

    starts = []
    ends = []
    skip = 0

    for y in range(N):
        S, E = map(int, input().split())
        starts.append(S)
        ends.append(E)

    starts.sort()
    ends.sort()
    deploys = 0
    endIndex = 0
    for start in starts:
        if skip == 0:
            target = start + K 
            deploys +=1
            for end in ends[endIndex:]:
                if end < target:
                    endIndex += 1

                elif end >= target:
                    break
        else: 
            skip -= 1

        
        if endIndex + 1 == len(ends):
            break




    dict.update({x+1: deploys})


for case, deployments in dict.items():
    print("Case #{}:".format(case) , deployments)  
    sys.stdout.flush()


    #boboquack answer
    # cases=int(input())
    # for case in range(1,cases+1):
    #     n,k=map(int,input().split())
    #     l=[list(map(int,input().split())) for i in range(n)]
    #     l.sort()
    #     r=0
    #     t=0
    #     for s,e in l:
    #         if t>=e:continue
    #         if t<=s:
    #             d=(e-s+k-1)//k
    #             r+=d
    #             t=s+d*k
    #         else:
    #             d=(e-t+k-1)//k
    #             r+=d
    #             t+=d*k
    #     print('Case #',case,': ',r,sep='')
