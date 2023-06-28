# 二分法

## Python
### [left, right]
```
class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle
        return -1

```


### [left, right)
```
class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        left = 0
        right = len(nums)   # 不-1， 因为右开
        while left < right:
            middle  = (left + right) // 2
            if target < nums[middle]:
                right = middle  # ..., right)
            elif target > nums[middle]:
                left = middle + 1  # [left, ...
            else:
                return middle
        return -1
```

## C++
### [left, right]
```
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // [left, right]
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (nums[middle] == target) {
                return middle;
            }
            else if (nums[middle] < target) {
                left = middle + 1;
            }
            else if (nums[middle] > target) {
                right = middle - 1;
            }
        }
        return -1;
    }
};
```


### [left, right)
```
class Solution {
public:
    int search(vector<int>& nums, int target) {
        // [left, right)
        int left = 0;
        int right = nums.size();

        while (left < right) {
            int middle = (left + right) / 2;
            if (target == nums[middle]) {
                return middle;
            }
            else if (target < nums[middle]) {
                right = middle;
            }
            else if (target > nums[middle]) {
                left = middle + 1;
            }
        }
        return -1;
    }
};
```

