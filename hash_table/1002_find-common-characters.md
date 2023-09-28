# 1002.查找常用字符
[Leetcode](https://leetcode-cn.com/problems/find-common-characters/)

## 题目
给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（包括重复字符, 也需重复返回），并以数组形式返回。你可以按 任意顺序 返回答案。

提示:  
* 1 <= words.length <= 100
* 1 <= words[i].length <= 100
* words[i] 由小写英文字母组成

## 解法: 
* 使用 min_count 存储每个字符在所有字符串中出现次数的最小值 
* 依次遍历每一个字符串，并记录每个字符的出现次数：
    * 每遍历一个字符串，就使用word_count统计该字符串中每一个字符出现的次数
    * 每统计完一个字符串，就将min_count与word_count相比较，并取每个字符频率最小值
* 当遍历完所有字符串后，min_count就存储了每个字符在所有字符串中出现次数的最小值

![1002.查找常用字符](https://code-thinking.cdn.bcebos.com/pics/1002.查找常用字符.png)


性能
* 时间复杂度: $O(n(m+|\Sigma|))$。其中n是字符串的数目，m是字符串的平均长度，$\Sigma$ 为字符集，在本题中字符集为所有小写字母，$\Sigma|=26$。  
    * 遍历所有字符串并计算word_count的时间复杂度为$O(nm)$；
    * 使用word_count更新min_count的时间复杂度为$O(n|\Sigma|)$；
    * 由于最终答案包含的字符个数不会超过最短的字符串长度，因此构造最终答案的时间复杂度为$O(m+|\Sigma|)$。这一项在渐进意义上小于前二者，可以忽略。
* 空间复杂度：$O(|\Sigma|)$，这里只计算存储答案之外的空间。我们使用了数组word_count和min_count，它们的长度均为$|\Sigma|$。


## C++
```
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> min_count(26, INT_MAX);
        vector<int> word_count(26,0);
        for (const string& word: words) {
            for (int i = 0; i < word.size(); i++) {
                word_count[word[i] - 'a']++;
            }
            for (int j = 0; j < 26; j++) {
                min_count[j] = min(min_count[j], word_count[j]);
            }
            fill(word_count.begin(), word_count.end(), 0);
        }

        vector<string> results;
        for (int k = 0; k < 26; k++) {
            while (min_count[k] != 0) {
                /*
                results.emplace_back(1, i+'a');
                // or
                string s(1, i+'a');
                results.emplace_back(s);
                // or
                string s = {char(i+'a')};
                results.emplace_back(s);
                */
                results.emplace_back(1, k+'a');
                min_count[k]--;
            }
        }
        
        return results;
    }
};
```

## Python
```
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_count = [float('inf')] * 26
        for word in words:
            word_count  = [0] * 26
            for i in range(len(word)):
                word_count[ord(word[i]) - ord('a')] += 1
            for i in range(26):
                min_count[i] = min(min_count[i], word_count[i])

        results = []
        for i in range(26):    
            results.extend([chr(i + ord('a'))] * min_count[i])
            # or
            # for j in range(min_count[i]):
            #     results.append(chr(i + ord('a')))
        return results
```
