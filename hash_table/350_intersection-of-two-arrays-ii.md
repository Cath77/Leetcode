# 350.两个数组的交集II
[Leetcode](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

## 题目
给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

提示:  
* 1 <= nums1.length, nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= 1000

## 解法:  
* 哈希表计数法
    * 思路
        * 首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数
        * 然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。
        * 为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。
    * 性能
        * 时间复杂度：$O(m+n)$，其中 m 和 n 分别是两个数组的长度。需要遍历两个数组并对哈希表进行操作，哈希表操作的时间复杂度是 $O(1)$，因此总时间复杂度与两个数组的长度和呈线性关系。
        * 空间复杂度：$O(\min(m,n))$，其中 m 和 n 分别是两个数组的长度。对较短的数组进行哈希表的操作，哈希表的大小不会超过较短的数组的长度。为返回值创建一个数组results，其长度不会超过较短的数组的长度。
* 排序 + 双指针
    * 思路
        * 首先对两个数组进行排序，然后使用两个指针遍历两个数组
        * 初始时，两个指针分别指向两个数组的头部
        * 每次比较两个指针指向的两个数组中的数字
            * 如果两个数字不相等，则将指向较小数字的指针右移一位
            * 如果两个数字相等，将该数字添加到答案，并将两个指针都右移一位
            * 当至少有一个指针超出数组范围时，遍历结束
    * 性能
        * 时间复杂度：$O(m \log m+n \log n)$，其中 m 和 n 分别是两个数组的长度。对两个数组进行排序的时间复杂度是 $O(m \log m+n \log n)$，遍历两个数组的时间复杂度是 $O(m+n)$，因此总时间复杂度是 $O(m \log m+n \log n)$。
        * 空间复杂度：$O(\min(m,n))$，其中 m 和 n 分别是两个数组的长度。为返回值创建一个数组 results，其长度不会超过较短的数组的长度。


## C++
```
// 哈希表计数法
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }
        
        unordered_map<int, int> record;
        for (const int& num: nums1) {
            record[num]++;
        }

        vector<int> results;
        for (const int& num: nums2) {
            if (record[num]) {
                record[num]--;
                results.emplace_back(num);
            }
        }
        
        return results;
    }
};
```

```
// 排序 + 双指针
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        vector<int> results;
        int idx1 = 0, idx2 = 0;
        while (idx1 < nums1.size() && idx2 < nums2.size()) {
            if (nums1[idx1] == nums2[idx2]) {
                results.emplace_back(nums1[idx1]);
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
        return results;   
    }
};
```

## Python
```
# 哈希表计数法
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        record = collections.Counter(nums1)

        results = list()
        for i in nums2:
            if record[i]:
                results.append(i)
                record[i] -= 1
        
        return results
```

```
# 排序 + 双指针
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        results = list()

        idx1, idx2 = 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                results.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        
        return results
```