# 34. 在排序数组中查找元素的第一个和最后一个位置
[Leetcode](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

## 题目
给你一个按照**非递减顺序排列**的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。  
如果数组中不存在目标值 target，返回 [-1, -1]。  
你必须设计并实现时间复杂度为 $O(log n)$ 的算法解决此问题。

提示：  
* nums 是一个非递减数组
* nums 可能包含重复元素，即 ```nums[i] <= nums[i + 1]```

解法:
* 首先，在 nums 数组中二分查找 target；
* 如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
* 如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间

## C++
```
class Solution {
public:
    int binarySearch(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        while (start <= end) {
            int middle = (start + end) / 2;
            if (nums[middle] < target) {
                start = middle + 1;
            }
            else if (nums[middle] > target) {
                end = middle - 1;
            }
            else {
                return middle;
            }
        }
        return -1;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        int idx = 0;
        idx = binarySearch(nums, target);
        if (idx == -1) {
            return {-1, -1};
        }
        else {
            int left = idx;
            int right = idx;
            while ((left - 1 >= 0) && (nums[left - 1] == target)) {
                left--;
            }
            while ((right + 1 <= nums.size() - 1) && (nums[right + 1] == target)) {
                right++;
            }
            return {left, right};
        }
    }
};
```


## Python
```
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(self, nums: List[int], target: int) -> int:
            start = 0
            end = len(nums) - 1
            while start <= end:
                middle = (start + end) // 2
                if nums[middle] > target:
                    end = middle - 1
                elif nums[middle] < target:
                    start = middle + 1
                else:
                    return middle
            return -1

        idx = binary_search(self, nums, target)
        if idx == -1:
            return [-1, -1]
        else:
            left, right = idx, idx
            while left - 1 >= 0 and nums[left - 1] == target:
                left -= 1
            while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
            return [left, right]

```