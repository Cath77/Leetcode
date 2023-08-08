# 844. 比较含退格的字符串
[Leetcode](https://leetcode.cn/problems/backspace-string-compare/)

## 题目
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。  
注意：如果对空文本输入退格字符，文本继续为空。

提示:  
* 1 <= s.length, t.length <= 200
* s 和 t 只含有小写字母以及字符 '#'

## 解法:  
* 

性能
* 时间复杂度: $O(n)$  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        // string s
        int s_slow = 0, s_fast = 0;
        while (s_fast < s.length()) {
            if (s[s_fast] != '#') {
                s[s_slow++] = s[s_fast++];
            }
            // s[s_fast] == '#'
            else {
                if (s_slow > 0) {
                    s_slow--;
                }
                s_fast++;
            }
        }

        // string t
        int t_slow = 0, t_fast = 0;
        while (t_fast < t.length()) {
            if (t[t_fast] != '#') {
                t[t_slow++] = t[t_fast++];
            }
            // t[t_fast] == '#'
            else {
                if (t_slow > 0) {
                    t_slow--;
                }
                t_fast++;
            }
        }

        // compare
        if (s_slow != t_slow) {
            return false;
        }
        else { 
            for (int idx = 0; idx < s_slow; idx++) {
                if (s[idx] != t[idx]) {
                    return false;
                }
            }
            return true;
        }
    }
};
```

```
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string ss = build(s);
        string tt = build(t);
        if (ss != tt) {
            return false;
        }
        else {
            return true;
        }
    }

    string build(string str) {
        int str_slow = 0, str_fast = 0;
        while (str_fast < str.length()) {
            if (str[str_fast] != '#') {
                str[str_slow++] = str[str_fast++];
            }
            // s[s_fast] == '#'
            else {
                if (str_slow > 0) {
                    str_slow--;
                }
                str_fast++;
            }
        }
        string sub = str.substr(0, str_slow);
        return sub;
    }
};
```

## Python
```
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s_slow, s_fast = 0, 0
        while s_fast < len(s):
            if s[s_fast] != "#":
                s[s_slow] = s[s_fast]
                s_slow += 1
                s_fast += 1
            else:
                if s_slow > 0:
                    s_slow -= 1
                s_fast += 1

        t_slow, t_fast = 0, 0
        while t_fast < len(t):
            if t[t_fast] != "#":
                t[t_slow] = t[t_fast]
                t_slow += 1
                t_fast += 1
            else:
                if t_slow > 0:
                    t_slow -= 1
                t_fast += 1

        if s[:s_slow] == t[:t_slow]:
            return True
        else:
            return False


```


```
class Solution:
    def get_string(self, s:str) -> str:
        s = list(s)
        s_slow, s_fast = 0, 0
        while s_fast < len(s):
            if s[s_fast] != "#":
                s[s_slow] = s[s_fast]
                s_slow += 1
                s_fast += 1
            else:
                if s_slow > 0:
                    s_slow -= 1
                s_fast += 1
        return str(s[:s_slow])


    def backspaceCompare(self, s: str, t: str) -> bool:
        s_result = self.get_string(s)
        t_result = self.get_string(t)

        if s_result == t_result:
            return True
        else:
            return False


```
