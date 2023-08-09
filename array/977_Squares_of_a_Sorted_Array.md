# 977.有序数组的平方
[Leetcode](https://leetcode.cn/problems/squares-of-a-sorted-array/)

## Python
```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [float('inf')] * len(nums)
        left = 0
        right = len(nums) - 1
        k = len(nums) - 1
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                result[k] = nums[right] ** 2
                right -= 1
            else:
                result[k] = nums[left] ** 2
                left += 1
            k -= 1
        return result
```


## C++
### For Loop
```
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int k = nums.size() - 1;
        vector<int> result(nums.size(), 0);
        for(int l = 0, r = nums.size() - 1; l <= r;) {
            if (nums[l] * nums[l] < nums[r] * nums[r]) {
                result[k--] = nums[r] * nums[r];
                r--;
            }
            else {
                result[k--] = nums[l] * nums[l];
                l++;
            }
        }
        return result;
    }
};
```

### While Loop
```
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int l = 0;
        int r = nums.size() - 1;
        int k = nums.size() - 1;
        vector<int> result(nums.size(), 0);
        while (l <= r) {
            if (nums[l] * nums[l] < nums[r] * nums[r]) {
                result[k--] = nums[r] * nums[r];
                r--;
            }
            else {
                result[k--] = nums[l] * nums[l];
                l++;
            }
        }
        return result;
    }
};
```