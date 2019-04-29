# Java real solution - using Dynamic Programming Longest Common Subsequence.

# class Solution {
#     public int maxUncrossedLines(int[] A, int[] B) {
#         int m = A.length;
#         int n = B.length;
#         int[][] dp = new int[m+1][n+1];
        
#         for (int i = 1; i< m+1; i++){
#             for (int j = 1; j < n+1; j++){

#                 if(A[i-1] == B[j-1]){
#                     dp[i][j] = 1 + dp[i-1][j-1];
#                    // System.out.println("match" + dp[i][j]); 
#                 }
#                 else{
#                     dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
#                     // System.out.println(dp[i][j]); 
#                 }
#             }
#         }
#         return dp[m][n];
    
#     }
# }


# Python fail at literal solution. Can't try every order, no mathematical shortcut that I know.

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        pairs = [];
       
        
        ans = 0
        
        for indexA in xrange(0, len(A)):
            for indexB in xrange(0, len(B)):
                if A[indexA] == B[indexB]:
                    pairs.append([indexA, indexB])
       
        for x in xrange(0, len(pairs)):
            print pairs
            excl = [];
            tot = 0;
            for pair in pairs:
                if pair in excl:
                    continue
                else:
                    tot = tot+ 1
                    for a in xrange(0, pair[0]+1):
                        for b in xrange(pair[1], len(B)):
                            excl.append([a, b])
                    for a in xrange(pair[0], len(A)):
                        for b in xrange(0, pair[1]+1):
                            excl.append([a, b])
                    if tot > ans:
                        ans = tot
                        print ans, tot
            pairs.insert(0, pairs.pop())
        
        return ans