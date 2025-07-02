class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        t1, t2, t3 = 0, 1, 1
        for _ in range(3, n+1):
            tNext = t1+t2+t3
            t1, t2, t3 = t2, t3, tNext
        return tNext


obj = Solution()
print(obj.tribonacci(4))
