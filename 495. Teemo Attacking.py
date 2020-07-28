class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        end = total = 0
        for t in timeSeries:
            if t > end:
                total += duration
            else:
                total += (duration - (end - t))
            end = t+duration
        return total