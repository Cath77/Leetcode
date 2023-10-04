# 263.丑数
[Leetcode](https://leetcode-cn.com/problems/ugly-number/)

## 题目
丑数 就是只包含质因数 2、3 和 5 的正整数。
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

提示:  
* $-2^{31}$ <= n <= $2^{31} - 1$

## 解法:  
* 方法
  * 思路
    * 根据丑数的定义，0 和负整数一定不是丑数。
    * 当 n>0 时，若 n 是丑数，则 n 可以写成 $n = 2^a \times 3^b \times 5^c$的形式，其中 a,b,c都是非负整数。特别地，当 a,b,c都是 0 时，n=1。
    * 为判断 n 是否满足上述形式，可以对 n反复除以 2,3,5，直到 n不再包含质因数 2,3,5。
        * 若剩下的数等于 1，则说明 n 不包含其他质因数，是丑数；
        * 否则，说明 n 包含其他质因数，不是丑数。
  * 性能
    * 时间复杂度: $O(\log n)$。时间复杂度取决于对 n 除以 2,3,5 的次数，由于每次至少将 n 除以 2，因此除法运算的次数不会超过 $O(\log n)$。
    * 空间复杂度: $O(1)$

## C++
```
class Solution {
public:
    bool isUgly(int n) {
      if (n <= 0) {
        return false;
      }
      else {
        int factors[] = {2, 3, 5};
        for (const auto& factor: factors) {
          while (n % factor == 0) {
            n = n / factor;
          }
        }
        return n==1;
      }
    }
};
```

## Python
```
# 官方解法
class Solution:
    def isUgly(self, n: int) -> bool:
      if n <= 0:
        return False

      div = [2, 3, 5]
      for factor in div:
        while n % factor == 0:
          n /= factor
        
      return n == 1
```

```
# 自己的解法
class Solution:
    def isUgly(self, n: int) -> bool:
        div = [2, 3, 5]
        tmp = float('inf')
        while float(n).is_integer() and tmp != n:
            tmp = n
            for x in div:
                if n % x == 0:
                    n /= x
        
        return n == 1
```