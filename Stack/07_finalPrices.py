class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        answer = prices[:]
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                answer[idx] = prices[idx] - prices[i]
            stack.append(i)

        return answer


sol = Solution()
result = sol.finalPrices([8, 4, 6, 2, 3])
print(result)
