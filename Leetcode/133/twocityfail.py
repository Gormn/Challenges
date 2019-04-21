import itertools
import sys

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs)/2
        min = sys.maxint
        cityA = []
        cityB = []
        
        for cost in costs:
            if (cost[0] < cost[1]):
                cityA.append(cost)
            else:
                cityB.append(cost)
                
        dif = 0
        if len(cityA) > len(cityB):
            dif = len(cityA) - N
            cityA.sort(key = lambda x: x[1])
            print cityA
            for i in xrange(0, dif):
                cityB.append(cityA[i])
                cityA.remove(cityA[i])
                
        elif len(cityA) < len(cityB):
            dif = len(cityB) - N 
            cityB.sort(key = lambda x: x[0])
            for i in xrange(0, dif):
                cityA.append(cityB[i])
                cityB.remove(cityB[i])
        
        aSum = sum(x[0] for x in cityA)
        bSum = sum(y[1] for y in cityB)
        
        tot = aSum + bSum
        
        return tot