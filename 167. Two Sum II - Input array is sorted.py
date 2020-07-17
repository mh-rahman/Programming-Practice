class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n1 in enumerate(numbers):
            n2 = target-n1
            j = bisect.bisect(numbers, n2, i+1,len(numbers))
            if j-1 >= len(numbers) or numbers[j-1] != n2 or i == j-1:
                continue
            return [i+1,j]
