# 258.各位相加
[Leetcode](https://leetcode-cn.com/problems/add-digits/)

## 题目
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

提示:  
* 0 <= num <= $2^{31} - 1$

## 解法:  
* 方法
  * 思路
    * 计算sum: 通过反复除10，得到位数与余数，用于计算sum
    * 反复相加，直到sum为一位数
  * 性能
    * 时间复杂度：$O(\log \textit{num})$，其中 num 是给定的整数
    * 空间复杂度：$O(1)$

## C++
```
class Solution {
public:
    int add_func(int num) {
      int sum = 0;
      while (num != 0) {
        sum += num % 10;
        num = int(num / 10);
      }
      return sum;
    }

    int addDigits(int num) {
      while (num / 10 != 0) {
        num = add_func(num);
      }
      return num;
    }
};
```

## Python
```
class Solution:
    def addFunc(self, num: int) -> int:
      sum = 0
      while num != 0:
        num, res = divmod(num, 10)
        sum += res
      return sum
    def addDigits(self, num: int) -> int:
      while num//10 != 0:
        num = self.addFunc(num)
      return num
```