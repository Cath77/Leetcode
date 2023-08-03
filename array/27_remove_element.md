# 移除元素
[Leetcode](https://leetcode.cn/problems/remove-element/)

* 数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖
* A difference between for loop in Python and for loop in C++ is that in C++, you can modify the counter variable or the range within the body of the loop. In Python, you cannot modify the counter variable or the range within the body of the loop.

## Python
* 双向指针法  
时间复杂度: O(n)  
空间复杂度: O(1)
```
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow_idx = 0
        fast_idx = len(nums) - 1
        while slow_idx <= fast_idx:
            while (slow_idx <= fast_idx) and (nums[slow_idx] != val):   # 必须(slow_idx <= fast_idx), 如果只是'<', 无法判别最后两个idx, 陷入死循环
                slow_idx += 1
            while (slow_idx <= fast_idx) and (nums[fast_idx] == val):   # 必须(slow_idx <= fast_idx), 如果只是'<', 无法判别最后两个idx, 陷入死循环
                fast_idx -= 1
            if (slow_idx < fast_idx) and (nums[slow_idx] == val) and (nums[fast_idx] != val):
                nums[slow_idx] = nums[fast_idx]
                slow_idx += 1   # 可选, 此处如果不+1, 前面的while loop也会再次检查后+1
                fast_idx -= 1   # 必要, 此处如果不+1, fast_idx就会一直停在这里
        return slow_idx
```


* 快慢指针法  
时间复杂度: O(n)  
空间复杂度: O(1)
```
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow_idx = 0
        fast_idx = 0
        nums_len = len(nums)
        while fast_idx < nums_len:
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast_idx] != val:
                nums[slow_idx] == nums[fast_idx]
                slow_idx += 1
            fast_idx += 1
        return slow_idx
```


* 暴力解法  
时间复杂度: O(n^2)  
空间复杂度: O(1)
```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        nums_len = len(nums)
        while i in range(0, nums_len):
        # 不用for i in range(0, nums_len), 因为loop中对i和nums_len的任何更新都不会改变for中相应的值
            if nums[i] == val:
                for j in range(i, nums_len - 1):
                    nums[j] = nums[j + 1]
                i -= 1
                nums_len -= 1
            i += 1
        return nums_len
```

## C++
* 双向指针法  
```
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            while ((left <= right) and (nums[left] != val)) {
                left ++;
            }
            while ((left <= right) and (nums[right] == val)) {
                right --;
            }
            if ((left <= right) and (nums[left] == val) and (nums[right] != val)) {
                nums[left] = nums[right];
                right --;
            }
        }
        return left;
    }
};
```

* 双指针法  
```
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0;
        for(int right = 0; right < nums.size(); right++) {  // 如果right <= nums.size() - 1, 空list时会出错,因为nums.size() - 1为-1,属于无效地址
            if (nums[right] != val) {
                nums[left] = nums[right];
                left ++;
            }
        }
        return left;
    }
};
```
