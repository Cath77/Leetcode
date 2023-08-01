# 35.搜索插入位置
[Leetcode](https://leetcode.cn/problems/search-insert-position/)

## 题目
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

必须使用时间复杂度为 O(log n) 的算法

提示:
* nums 为**无重复元素**的**升序**排列数组
* 1 <= nums.length <= $10^4$
* $-10^4$ <= nums[i] <= $10^4$
* $-10^4$ <= target <= $10^4$


## C++
```
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        while (start <= end) {
            int middle = (start + end) / 2;
            if (nums[middle] > target) {
                end = middle - 1;
            }
            else if (nums[middle] < target) {
                start = middle + 1;
            }
            else {
                return middle;
            }
        }
        return start;
    }
};
```


## Python
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        return start
```