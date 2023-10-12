# 1.两数之和
[Leetcode](https://leetcode-cn.com/problems/two-sum/description/)

## 题目
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那 **两个** 整数，并返回它们的数组下标。  
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现（即不能让元素与自己匹配构成答案，如3与自己相加可构成target = 6）。

提示:  
* 2 <= nums.length <= $10^4$
* $-10^$ <= nums[i] <= $10^9$
* $-10^9$ <= target <= $10^9$
* **只会存在一个有效答案**

## 解法:  
* 方法一：哈希表法
  * 思路
    * 遍历数组，对于每个元素nums[i]，查找target - nums[i]是否存在于哈希表中
      * 如果存在，则返回对应的下标
      * 如果不存在，则将nums[i]作为key加入哈希表中，其对应的下标作为value
  * 性能
    * 时间复杂度: $O(n)$，其中 n 是数组中的元素数量。对于每一个元素 x，我们可以 $O(1)$ 地寻找 target - x。  
    * 空间复杂度: $O(n)$，其中 n 是数组中的元素数量。主要为哈希表的开销。
* 方法二：双指针法
  * 性能
    * 时间复杂度: $O(nlogn)$，
    * 空间复杂度：$O(n)$。


## C++
```
// 哈希表法：unordered_map
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> records;
        for (int i = 0; i < nums.size(); i++) {
            if (records.contains(target - nums[i])) {
                return {records[target - nums[i]], i};
            }
            else {
                records[nums[i]] = i;
            }
        }
        return {};
    }
};
```

## Python
```
// 哈希表法：字典
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        # records = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            if (target - num) in records.keys():
                return [records[target - num], idx]
            else:
                records[num] = idx
        return list()
```

```
// 双指针法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(zip(nums, range(len(nums))))

        left, right = 0, len(nums) - 1
        while left < right:
                sums = nums[left][0] + nums[right][0]
                if sums == target:
                    return [nums[left][1], nums[right][1]]
                elif sums > target:
                    right -= 1
                else:
                    left += 1
        return []
```
