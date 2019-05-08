class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ans = []
        freq = {}
        index = 0
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        
        for f in sorted(freq.items(), key = lambda x: (-x[1], x[0])):
            ans.append(f[0]);
            index += 1
            if index >= k:
                return ans
        
        return ans


class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]

        for f in sorted(c.items(), key = lambda x: (-x[1], x[0])):
            ans.append(f[0])
            index +=1;
            if index >= k:
                return ans


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.Counter(nums)
        ans = dic.keys();
        ans.sort(key = lambda x: -dic[x])
        return ans[:k]

    n = int(raw_input())
    for _ in xrange(n):
        a, b = map(int, raw_input().strip().split())
        print a + b


    ans = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if ans and i[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], i[1])
        else:
            ans += i,
    
    return ans

    favs = {}
    ans = []
    index = -1
    
    for i in xrange(0, len(list1)):
        for x in xrange(0, len(list2)):
            if list1[i] == list2[x]:
                place = list1[i]
                dex = x+i
                if index < 0:
                    ans.append(place)
                    index = dex
                elif dex < index:
                    ans = []
                    ans.append(place)
                    index = dex
                elif dex == index:
                    ans.append(place)

    return ans

        