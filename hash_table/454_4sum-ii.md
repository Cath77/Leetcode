# 454.四数相加II
[Leetcode](https://leetcode-cn.com/problems/4sum-ii/)

## 题目
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (a, b, c, d) 能满足：
* 0 <= a, b, c, d < n
* nums1[a] + nums2[b] + nums3[c] + nums4[d] == 0

提示:  
* n == nums1.length == nums2.length == nums3.length == nums4.length
* 1 <= n <= 200
* $-2^28$ <= nums1[i], nums2[i], nums3[i], nums4[i] <= $2^28$

## 解法:  
* 哈希表
  * 思路
    * 首先定义 一个unordered_map，key放a和b两数之和，value 放a和b两数之和出现的次数。
    * 遍历大A和大B数组，统计两个数组元素之和，和出现的次数，放到map中。
    * 定义int变量count，用来统计 a+b+c+d = 0 出现的次数。
    * 在遍历大C和大D数组，找到如果 0-(c+d) 在map中出现过的话，就用count把map中key对应的value也就是出现次数统计出来。
    * 最后返回统计值 count 就可以了
  * 性能
    * 时间复杂度: $O(n^2)$  
    * 空间复杂度: $O(n^2)$, 最坏情况下A和B的值各不相同，相加产生的数字个数为 $n^2$


## C++
```
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> record_ab;
        for (const auto& a : nums1) {
            for (const auto& b : nums2) {
                record_ab[a + b]++;
            }
        }

        int count = 0;
        for (const auto& c : nums3) {
            for (const auto& d : nums4) {
                if (record_ab.find(-(c + d)) != record_ab.end()) {
                    count += record_ab[-(c + d)];
                }
            }
        }
        return count;
    }
};
```

## Python
```
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        records_ab = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                records_ab[a + b] += 1

        counts = 0
        for c in nums3:
            for d in nums4:
                counts += records_ab.get(-(c+d), 0)

        return counts
```
