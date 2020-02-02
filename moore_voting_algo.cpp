//Keep track of a major number which is basically a number that has occured more than n/2 times till that index.
//If current number equals major number, increase count else decrease count.
//If count reaches negative start afresh.

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int major, counts = 0, n = nums.size();
        for (int i = 0; i < n; i++) {
            if (counts<=0 ) {
                major = nums[i];
                counts = 1;
            }
            else counts += (nums[i] == major) ? 1 : -1;
        }
        return major;
    }
};