class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        Q, currSum, minLen = deque([]), 0, math.inf
        for n in nums:
            Q.append(n)
            currSum += n
            if currSum >= s: minLen = min(minLen, len(Q))
            while Q and currSum - Q[0] >= s:
                currSum = currSum - Q.popleft()
                minLen = min(minLen, len(Q))
        return 0 if minLen > len(nums) else minLen