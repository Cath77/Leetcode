# 69. x的平方根
[Leetcode](https://leetcode.cn/problems/sqrtx/)

## 题目
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。  
由于返回类型是**整数**，结果只保留**整数部分**，小数部分将被**舍去**。  
注意：不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。

提示：
$0 <= x <= 2^{31} - 1$

## C++
```
class Solution {
public:
    int mySqrt(int x) {
        int start = 0;
        int end = x;
        while (start <= end) {
            int middle = (start + end) / 2;
            // (long long)为了防止溢出
            // mid数据类型是int，mid*mid存在溢出int的可能性
            if ((long long)middle * middle < x) {
                start = middle + 1;
            }
            else if ((long long)middle * middle > x) {
                end = middle - 1;
            }
            else {
                return middle;
            }
        }
        return end;
    }
};
```


## Python
```
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            middle = (start + end) // 2
            if int(middle * middle) > x:
                end = middle - 1
            elif int(middle * middle) < x:
                start = middle + 1
            else:
                return middle
        return end
```