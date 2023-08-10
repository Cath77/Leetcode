# 209.长度最小的子数组
[Leetcode](https://leetcode.cn/problems/minimum-size-subarray-sum/)

## Python
```
# 官方解答
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

```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        cur_sum = 0
        min_len = float('inf')

        while end < len(nums):
            cur_sum += nums[end]
            end += 1

            if cur_sum >= target and cur_sum - nums[start] < target:
                cur_len = end - start
                min_len = min(cur_len, min_len)

            while cur_sum >= target and cur_sum - nums[start] >= target:
                cur_sum -= nums[start]
                start += 1
                cur_len = end - start
                min_len = min(cur_len, min_len)

        return min_len if min_len != float('inf') else 0
```

## C++
```
// 官方解答
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

```
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int start = 0;
        int end = 0;
        int min_len = INT32_MAX;
        int sum = 0;
        while (end < nums.size()) {
            sum += nums[end++];
            if (sum >= target && sum - nums[start] < target) {
                min_len = min_len > (end - start) ? (end - start) : min_len;
            }
            while (sum >= target && sum >= target + nums[start]) {
                sum -= nums[start++];
                min_len = min_len > (end - start) ? (end - start) : min_len;
            }
        }
        return min_len != INT32_MAX ? min_len : 0;
    }
};
```