# 904. 水果成篮
[Leetcode](https://leetcode.cn/problems/fruit-into-baskets/)

## 题目
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：

你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。

提示:  
* 1 <= fruits.length <= 105
* 0 <= fruits[i] < fruits.length

## 解法:  
* 方法：滑动窗口与哈希表
  * 思路
    * left 和 right 分别表示满足要求的窗口的左右边界，同时我们使用哈希表存储这个窗口内的数以及出现的次数。
    * 每次将 right 移动一个位置，并将 fruits[right] 加入哈希表。
        * 如果此时哈希表中出现超过两个键值对，则不断移动 left，将fruits[left]从哈希表中移除，直到哈希表重新满足长度为2。
            * 需要注意的是，将 fruits[left] 从哈希表中移除后，如果 fruits[left] 在哈希表中的出现次数减少为 0，需要将对应的键值对从哈希表中移除。
        * 取满足条件的窗口的最大宽度。
  * 性能
    * 时间复杂度: $O(n)$，其中 n 是数组 fruits 的长度。
    * 空间复杂度: $O(1)$，因为哈希表中最多只会存储 3 个键值对。


## C++
```
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int max_counts = 0;
        int left = 0;
        unordered_map<int, int> cur_counts;

        for (int right = 0; right < fruits.size(); right++) {
            cur_counts[fruits[right]]++;
            while (cur_counts.size() > 2) {
                cur_counts[fruits[left]]--;
                if (cur_counts[fruits[left]] == 0) {
                    cur_counts.erase(fruits[left]);
                }
                left++;
            }
            max_counts = max(max_counts, right - left + 1);
        }
        return max_counts;
    }
};
```

## Python
```
# 官方解法：滑动窗口
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cur_counts = collections.defaultdict(int)

        left = 0
        max_counts = float('-inf')
        for right, x in enumerate(fruits):
            cur_counts[x] += 1
            while len(cur_counts) > 2:
                cur_counts[fruits[left]] -= 1
                if cur_counts[fruits[left]] == 0:
                    cur_counts.pop(fruits[left])
                left += 1
            max_counts = max(max_counts, right - left + 1)
        
        return max_counts
```

```
# 自己的解法：滑动窗口
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(set(fruits)) <= 2:
            return len(fruits)

        cur_count = 0
        max_count = float('-inf')
        left_idx = 0
        right_idx = left_idx + 1

        while left_idx < right_idx and left_idx < len(fruits) and right_idx < len(fruits):
            tree1 = fruits[left_idx]
            while right_idx + 1 < len(fruits) and fruits[right_idx] == tree1:
                right_idx += 1
            tree2 = fruits[right_idx]
            tmp_idx = right_idx
            while right_idx + 1 < len(fruits) and fruits[right_idx + 1] in [tree1, tree2]:
                right_idx += 1

            cur_count = right_idx - left_idx + 1
            max_count = max(cur_count, max_count)
            left_idx = tmp_idx
            right_idx = left_idx + 1

        return max_count
```