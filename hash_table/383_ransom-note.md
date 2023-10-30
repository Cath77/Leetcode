# 383.赎金信
[Leetcode](https://leetcode.cn/problems/ransom-note/description/)

## 题目
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。magazine 中的每个字符只能在 ransomNote 中使用一次。<br>
如果可以，返回 true ；否则返回 false。


提示:  
* 1 <= ransomNote.length, magazine.length <= 105
* ransomNote 和 magazine 由小写英文字母组成

## 解法:  
* 方法：哈希表
  * 思路
    * 因为题目说只有小写字母，那可以用一个长度为26的数组来记录ransomNote里字母出现的次数
    * 然后再验证这个数组是否包含了magazine所需要的所有字母
  * 性能
    * 时间复杂度: $O(n)$  
    * 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int records_mg[26] = {0};
        if (ransomNote.size() > magazine.size()) return false;
        for (const auto& letter: magazine) {
            records_mg[letter-'a']++;
        }
        for (const auto& letter: ransomNote) {
            if (records_mg[letter - 'a'] <= 0) {
                return false;
            }
            else {
                records_mg[letter - 'a']--;
            }
        }
        return true;
    }
};          
```

## Python
```
# 数组
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        counts_mg = [0] * 26
        for letter in magazine:
            counts_mg[ord(letter) - ord('a')] += 1
        for letter in ransomNote:
            if counts_mg[ord(letter) - ord('a')] <= 0:
                return False
            else:
                counts_mg[ord(letter) - ord('a')] -= 1
        return True
```

```
# defaultdict()
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts_mg = collections.defaultdict(int)

        for letter in magazine:
            counts_mg[letter] += 1
        for letter in ransomNote:
            if letter in counts_mg:
                counts_mg[letter] -= 1
                if counts_mg[letter] < 0:
                    return False
            else:
                return False

        return True
```

```
# Counter()
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
```