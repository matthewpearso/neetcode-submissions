class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        N, M = len(s1), len(s2)
        
        dp = {}

        def search(i, j, k):
            if k >= len(s3):
                return True if i == N and j == M else False

            if (i, j) in dp:
                return dp[(i, j)]

            choose1 = search(i + 1, j, k + 1) if i < N and s1[i] == s3[k] else False
            choose2 = search(i, j + 1, k + 1) if j < M and s2[j] == s3[k] else False

            dp[(i, j)] = choose1 or choose2

            return dp[(i, j)]
        
        return search(0, 0, 0)

           
                