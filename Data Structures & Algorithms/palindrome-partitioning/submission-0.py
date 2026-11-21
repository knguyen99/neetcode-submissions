class Solution:
    def partition(self, s: str) -> List[List[str]]:
        slen = len(s)
        dp = [[False for _ in range(slen)] for _ in range(slen) ] 

        for i in range(slen):
            dp[i][i] = True
            if i > 0:
                if s[i] == s[i-1]:
                    dp[i-1][i] = True
        
        def expand(a,b):
            if a >= 0 and b < slen and s[a] == s[b]:
                dp[a][b] = True
                expand(a-1, b+1)
        
        for i in range(slen):
            expand(i,i)
            if i > 0 and dp[i-1][i]:
                expand(i-1,i)

        ret = []
        def backtrack(i, curr):
            if i == slen:
                ret.append(curr[:])
            else:
                for j in range(i, slen):
                    if dp[i][j]:
                        curr.append(s[i:j+1])
                        backtrack(j+1,curr)
                        curr.pop()
        backtrack(0,[])
        return ret
            



        
