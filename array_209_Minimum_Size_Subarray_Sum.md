# 209.长度最小的子数组

## Python
```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = 0
        min_len = float('inf')
        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        if min_len != float('inf'): return min_len
        else: return 0
```

## C++
```
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, right = 0;
        int sum = 0;
        int sub_len = INT32_MAX;
        while (right < nums.size()) {
            sum += nums[right];
            while (sum >= target) {
                int cur_len = right - left + 1;
                sub_len = sub_len > cur_len ? cur_len : sub_len;
                sum -= nums[left++];
            }
            right++;
        }
        return sub_len != INT32_MAX ? sub_len : 0;
    }
};
```