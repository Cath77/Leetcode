# 202.快乐数
[Leetcode](https://leetcode-cn.com/problems/happy-number/)

## 题目
编写一个算法来判断一个数 n 是不是快乐数。  

「快乐数」 定义为：  
* 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
* 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
* 如果这个过程 结果为 1，那么这个数就是快乐数。

如果 n 是 快乐数 就返回 true ；不是，则返回 false 。



## 解法:  
* 计算sum: 通过反复除10，得到位数与余数，用于计算sum
* 如果sum为1，则为快乐数
* 如果sum不为1，查找sum是否存在于set中
  * 如果已存在，代表产生循环，则该数不是快乐数
  * 如果不存在，则将sum加入set，继续循环

性能
* 时间复杂度: $O(log n)$  
* 空间复杂度: $O(log n)$


## C++
```
class Solution {
public:
    // 通过反复除10，得到位数与余数，用于计算sum
    int get_sum(int n) {
        int cur_sum = 0;
        while (n) {
            int res = n % 10;
            n = n / 10;
            cur_sum += res * res;
        }
        return cur_sum;
    }

    bool isHappy(int n) {
        unordered_set<int> sums;
        while(true) {
            int cur_sum = get_sum(n);
            // 如果sum为1，则为快乐数
            if (cur_sum == 1) {
                return true;
            }
            // 否则，查找sum是否存在于set中
            else {
                // 如果已存在，代表产生循环，则该数不是快乐数
                if (sums.contains(cur_sum)) {
                    return false;
                }
                // 如果不存在，则将sum加入set，继续循环
                else {
                    sums.emplace(cur_sum);
                    n = cur_sum;
                }
            }
        }
    }
};
```

## Python
```
class Solution:
    def sum(self, n: int) -> int:
        cur_sum = 0
        while n:
            # divmod(): takes two real numbers as arguments and returns a tuple consisting of quotient q and remainder r values.
            n, res = divmod(n, 10)
            # res = n % 10
            # n = int(n / 10)
            cur_sum += res**2
        return cur_sum            

    def isHappy(self, n: int) -> bool:
        sums = set()
        while True:
            cur_sum = self.sum(n)
            if cur_sum == 1:
                return True
            else:
                if cur_sum in sums:
                    return False
                else:
                    sums.add(cur_sum)
                    n = cur_sum
        
```

```
class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n not in sums:
            if n == 1:
                return True
            else:
                sums.add(n)
                cur_sum = 0
                while n:
                    n, res = divmod(n, 10)
                    cur_sum += res**2
                n = cur_sum
        return False
```
