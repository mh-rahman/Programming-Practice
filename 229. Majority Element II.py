class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
	
	    # Find a maximum of 2 candidate solutions
        c = {}
        for num in nums:
            if num in c:
                c[num] += 1
            elif len(c) < 2:
                c[num] = 1
            else:
			    # we found a 3th number that is not a candidate, 
				# instead of adding it to dict we lower the counts of the current candidates
				# we keep candidates with counts higher than 1
                c = {k: v - 1 for k, v in c.items() if v > 1}
        
		# check if the candidates occur more then L // 3 times
        return [k for k in c if nums.count(k) > len(nums) // 3]