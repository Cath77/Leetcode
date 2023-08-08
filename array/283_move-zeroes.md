# 283. 移动零
[Leetcode](https://leetcode.cn/problems/move-zeroes/)

## 题目


提示:  
* 

解法:  
* 双指针法：快慢指针
** 快指针遍历数组，慢指针指向第一个0元素
** 如遇到慢指针指向0，而快指针指向的元素不为0，则交换快慢指针指向的元素，慢指针后移


## C++
```
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        for (int fast = 0; fast < nums.size(); fast++) {
            while (nums[slow] != 0 and slow < fast) {
                slow++;
            }
            if (nums[slow] == 0 && nums[fast] != 0) {
                nums[slow++] = nums[fast];
                nums[fast] = 0;
            }
        }
    }
};
```

```
// 官方解答
// 非0，交换数据，左右指针都往右移
// 0，右指针右移

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        int fast = 0;
        while (fast < nums.size()) {
            if (nums[fast] != 0) {
                swap(nums[slow], nums[fast]);
                slow++;
            }
            fast++;
        }
    }
};
```

## Python
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            while (nums[slow] != 0) and (slow < fast):
                slow += 1
            if (nums[slow] == 0) and (nums[fast] != 0):
                nums[slow] = nums[fast]
                nums[fast] = 0
                slow += 1
            fast += 1
```

```
# 官方解答
# 非0，交换数据，左右指针都往右移
# 0，右指针右移

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
```