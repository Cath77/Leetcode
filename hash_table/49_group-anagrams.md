# 49.字母异位词分组
[Leetcode](https://leetcode-cn.com/problems/group-anagrams/description/)

## 题目
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。  
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

提示:  
* strs[i] 仅包含小写字母

## 解法:  
1. 排序
    * 思路
        * 将排序之后的字符串作为哈希表的键：由于互为字母异位词的两个字符串包含的字母相同，因此对两个字符串分别进行排序之后得到的字符串一定是相同的。
        * 将字母异位词存储为对应键的值。
    * 性能
        * 时间复杂度: $O(nklogk)$。其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。需要遍历 n 个字符串，对于每个字符串，需要 $O(klog⁡k)$ 的时间进行排序以及 $O(1)$ 的时间更新哈希表。因此总时间复杂度是 $O(nklog⁡k)$。
        * 空间复杂度：$O(nk)$，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度。需要用哈希表存储全部字符串。
        
2. 计数（同[242.有效的字母异位词](./242_valid-anagram.md)）
    * 思路
        * 将一个字符串中每个字母出现的次数使用数组来记录，然后将数组转换为哈希表的键。
        * 将字母异位词存储为对应键的值。
    * 性能
        * 时间复杂度：$O(n(k+|Σ|))$，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的的最大长度，$Σ$ 是字符集，在本题中字符集为所有小写字母，$|Σ|=26$。需要遍历 n 个字符串，对于每个字符串，需要 $O(k)$ 的时间计算每个字母出现的次数，$O(|Σ|)$ 的时间生成哈希表的键，以及 $O(1)$ 的时间更新哈希表，因此总时间复杂度是 $O(n(k+|Σ|))$。
        * 空间复杂度：$O(n(k+|Σ|))$，其中 n 是 strs 中的字符串的数量，k 是 strs 中的字符串的最大长度，$Σ$ 是字符集，在本题中字符集为所有小写字母，$|Σ|=26$。需要用哈希表存储全部字符串，而记录每个字符串中每个字母出现次数的数组需要的空间为 $O(|Σ|)$，在渐进意义下小于 $O(n(k+|Σ|))$，可以忽略不计。

## C++
```
// 方法1：排序
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> records;
        for(auto str : strs) {
            string key = str;
            sort(str.begin(), str.end());
            records[str].emplace_back(key);
        }
        vector<vector<string>> ans;
        for(const auto &kv : records) {
            ans.emplace_back(kv.second);
        }
        return ans;
    }
};

/*
Range-Based Loop:
// Traversing an unordered map
for (auto x : umap) {
    cout << x.first << " " << 
            x.second << endl;
}

auto T           // I'm copying this
auto &T          // I'm modifying this
const auto &T    // I'm reading this
*/
```

```
# 方法2：计数

```


## Python
```
# 方法1：排序
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = collections.defaultdict(list)
        for str in strs:
            # 将排序之后的字符串作为哈希表的键，然后将字母异位词存储为对应键的值。
            record["".join(sorted(str))].append(str)
        return list(record.values())
```

```
# 方法2：计数
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = collections.defaultdict(list)
        for st in strs:
            # 将一个字符串中每个字母出现的次数使用数组来记录
            count = [0] * 26
            for i in range(len(st)):
                count[ord(st[i]) - ord('a')] += 1
            # 将数组转换为哈希表的键，然后将字母异位词存储为对应键的值。
            record[tuple(count)].append(st)
        return list(record.values())
```
