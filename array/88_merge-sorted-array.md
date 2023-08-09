# 88. 合并两个有序数组
[Leetcode](https://leetcode.cn/problems/merge-sorted-array/)

## 题目
给你两个按 **非递减顺序** 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。  
请你 **合并** nums2 到 nums1 中，使合并后的数组同样按 **非递减顺序** 排列。  
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

提示:  
* nums1.length == m + n
* nums2.length == n
* 0 <= m, n <= 200
* 1 <= m + n <= 200
* $-10^9$ <= nums1[i], nums2[j] <= $10^9$
 

## 解法:  
* 逆向双指针

性能
* 时间复杂度: $O(m+n)$  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int end1 = m - 1, end2 = n - 1;
        int idx = m + n - 1;
        if (end1 == -1) {
            nums1  = nums2;
        }
        else if (end2 == -1) {
            return;
        }
        else {
            while (end1 >= 0 || end2 >= 0) {
                if (end1 == -1) {
                    nums1[idx--] = nums2[end2--];
                }
                else if (end2 == -1) {
                    nums1[idx--] = nums1[end1--];
                }
                else if (nums1[end1] <= nums2[end2]) {
                    nums1[idx--] = nums2[end2--];
                }
                else if (nums1[end1] > nums2[end2]) {
                    nums1[idx--] = nums1[end1--];
                }
            }   
        }
    }
};
```

```
// 官方解答
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int end1 = m - 1;
        int end2 = n - 1;
        int idx = nums1.size() - 1;

        while (end1 >= 0 || end2 >= 0) {
            if (end1 == -1) {
                nums1[idx--] = nums2[end2--];
            }
            else if (end2 == -1) {
                nums1[idx--] = nums1[end1--];
            }
            else if (nums1[end1] <= nums2[end2]) {
                nums1[idx--] = nums2[end2--];
            }
            else {
                nums1[idx--] = nums1[end1--];
            }
        }
    }
};
```

## Python
```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end1 = m - 1
        end2 = n - 1
        idx = len(nums1) - 1

        if end1 == -1:
            nums1[:] = nums2[:]
            return
        elif end2 == -1:
            return
        else:
            while end1 >= 0 or end2 >= 0:
                if end1 == -1:
                    nums1[idx] = nums2[end2]
                    idx -= 1
                    end2 -= 1
                elif end2 == -1:
                    nums1[idx] = nums1[end1]
                    idx -= 1
                    end1 -= 1
                elif nums1[end1] <= nums2[end2]:
                    nums1[idx] = nums2[end2]
                    idx -= 1
                    end2 -= 1
                else:
                    nums1[idx] = nums1[end1]
                    idx -= 1
                    end1 -= 1
                
```

```
# 官方解答
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end1 = m - 1
        end2 = n - 1
        idx = len(nums1) - 1

        while end1 >= 0 or end2 >= 0:
            if end1 == -1:
                nums1[idx] = nums2[end2]
                end2 -= 1
            elif end2 == -1:
                nums1[idx] = nums1[end1]
                end1 -= 1
            elif nums1[end1] <= nums2[end2]:
                nums1[idx] = nums2[end2]
                end2 -= 1
            else:
                nums1[idx] = nums1[end1]
                end1 -= 1
            idx -= 1
```