'''
Using a deque to store the indexes of num array as follows: 
The max of a sliding window will always be stored at the leftmost position, also the most earlier added to the deque.
When adding any entry to the list, we want to make sure any previous entries smaller than it are popped.
We start checking from the rightmost position.

Hence we got this pattern: in deque, indexes are increasing left to right while the values at those index are decreasing 
(as a higher index value failed to pop lower index value).

Also, as soon as the leftmost index in deque is out of the sliding window, we pop it (using popleft()).

Keep adding deque[0] to the result array (but only after the we have scanned at least K elements.
'''

def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out