# 242.有效的字母异位词
[Leetcode](https://leetcode-cn.com/problems/valid-anagram/description/)

## 题目
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。  
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

提示:  
* s 和 t 仅包含小写字母

## 解法:  
* 定义一个数组用来记录字符串里字符出现的次数
* 把字符映射到数组的索引下标上，即将字符a到字符z的ASCII码转换为数字0到25
* 先存s后删t，最后统计是否有数值不为0，如果有，则代表两个字符串所含有的字母不相同。

性能
* 时间复杂度: $O(n)$  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> record(26, 0);
        for (int i = 0; i < s.size(); i++) {
            record[s[i] - 'a'] += 1;
        }
        for (int i = 0; i < t.size(); i++) {
            record[t[i] - 'a'] -= 1;
            // if (record[t[i] - 'a'] == -1) return false;
        }
        for (int i = 0; i < record.size(); i++) {
            if (record[i] != 0) return false;
        }
        return true;
    }
};
```

## Python
```
# 使用数组作为哈希表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      record = [0] * 26
      for i in range(len(s)):
        record[ord(s[i]) - ord('a')] += 1
      for i in range(len(t)):
        record[ord(t[i]) - ord('a')] -= 1
      for i in range(len(record)):
        if record[i] != 0:
          return False

      return True  
```

```
# 使用字典作为哈希表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      from collections import defaultdict
      record = defaultdict(lambda: 0)
      for i in s:
        record[i] += 1
      for i in t:
        record[i] -= 1
        # if record[i] == -1:
        #   return False
      for i in list(record.values()):
        if i != 0:
          return False
      return True
```
