# 26. 删除有序数组中的重复项
[Leetcode](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

## 题目
给你一个**升序排列**的数组 nums ，请你**原地**删除重复出现的元素，使每个元素**只出现一次**，返回删除后数组的新长度。  
元素的**相对顺序应该保持一致**。然后返回 nums 中**唯一元素的个数**。

解法:  
* 快慢指针法


## C++
```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }
        else {
            int slow = 0;
            for (int fast = 1; fast < nums.size(); fast++) {
                if (nums[slow] != nums[fast]) {
                    nums[++slow] = nums[fast];
                }
            }
            return slow + 1;
        }

    }
};
```

```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow = 0;
        int fast = 1;
        while (fast < nums.size()) {
            if (nums[slow] == nums[fast]) {
                fast++;
            }
            else {
                nums[++slow] = nums[fast++];
            }
        }
        return slow + 1;
    }
};
```

## Python
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1
```