# 367. 有效的完全平方数
[Leetcode](https://leetcode.cn/problems/valid-perfect-square/)

## 题目
给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。  
完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。  
不能使用任何内置的库函数，如  sqrt 。

提示：
$1 <= num <= 2^{31} - 1$


## C++
```
class Solution {
public:
    bool isPerfectSquare(int num) {
        int start = 0;
        int end = num;
        while (start <= end) {
            int middle = (start + end) / 2;
            if ((long long)middle * middle > num) {
                end = middle - 1;
            }
            else if ((long long)middle * middle < num) {
                start = middle + 1;
            }
            else {
                return true;
            }
        }
        return false;
    }
};
```


## Python
```
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while start <= end:
            middle = (start + end) // 2
            if middle * middle > num:
                end = middle - 1
            elif middle * middle < num:
                start = middle + 1
            else:
                return True
        return False
```