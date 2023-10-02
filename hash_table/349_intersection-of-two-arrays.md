# 349. 两个数组的交集
[Leetcode](https://leetcode-cn.com/problems/intersection-of-two-arrays/)

## 题目
给定两个数组 nums1 和 nums2 ，返回它们的交集。输出结果中的每个元素一定是 **唯一** 的，不考虑输出结果的顺序。

提示:  
* 1 <= nums1.length, nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= 1000

## 解法:  
* 方法一：集合（与哈希表）
    * 思路
        * 使用两个set，或一个hash与set，求其交集
    * 性能
        * 时间复杂度: $O(m+n)$，其中 m 和 n 分别是两个数组的长度。   
        * 空间复杂度: $O(m+n)$，其中 m 和 n 分别是两个数组的长度。
* 方法二：排序 + 双指针
    * 思路
        * 首先对两个数组进行排序，然后使用两个指针遍历两个数组
        * 初始时，两个指针分别指向两个数组的头部
        * 每次比较两个指针指向的两个数组中的数字
            * 如果两个数字不相等，则将指向较小数字的指针右移一位
            * 如果两个数字相等，将该数字添加到set，并将两个指针都右移一位
            * 当至少有一个指针超出数组范围时，遍历结束
    * 性能
        * 时间复杂度: $O(mlogm+nlogn)$，其中 m 和 n 分别是两个数组的长度。
        * 空间复杂度: $O(logm+logn)$，其中 m 和 n 分别是两个数组的长度。


## C++
```
// 两个集合
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> records(nums1.begin(), nums1.end());
        unordered_set<int> results;

        for (const int& num: nums2) {
            if (records.contains(num)) {
                results.emplace(num);
            }
        }

        return vector<int>(results.begin(), results.end());
    }
};
```

```
// 一个集合与一个哈希表
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> record(1000, 0);
        for (const auto& num: nums1) {
            record[num] = 1;
        }

        unordered_set<int> results;
        for (const auto& num: nums2) {
            if (record[num] == 1) {
                results.emplace(num);
            }
        }

        return vector<int>(results.begin(), results.end());
    }
};
```

```
// 排序 + 双指针
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        unordered_set<int> results;
        int idx1 = 0, idx2 = 0;
        while (idx1 < nums1.size() && idx2 < nums2.size()) {
            if (nums1[idx1] == nums2[idx2]) {
                results.emplace(nums1[idx1]);
                idx1++;
                idx2++;
            }
            else if (nums1[idx1] < nums2[idx2]) {
                idx1++;
            }
            else {
                idx2++;
            }
        }

        return vector<int>(results.begin(), results.end());
    }
};
```

## Python
```
# 两个集合求交集
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
```

```
# 排序 + 双指针
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        results = set()
        idx1, idx2 = 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                results.add(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return list(results)
```
