# 54. 螺旋矩阵
[Leetcode](https://leetcode.cn/problems/spiral-matrix/)

## 题目
给你一个**m 行 n 列**的矩阵 matrix ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

提示:  
* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 10
* -100 <= matrix[i][j] <= 100

## 解法:  
* 

性能
* 时间复杂度: $O(mn)$，m 和 n 分别是输入矩阵的行数和列数。矩阵中的每个元素都要被访问一次。  
* 空间复杂度: $O(mn)$， 需要创建一个大小为 $m \times n$ l的矩阵记录每个位置是否被访问过。


## C++
```
// 自己写的
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        int startx = 0, starty = 0;
        int cur_round = 1, max_round = min(m, n) / 2;
        int idx_x, idx_y;
        vector<int>result (m*n, 0);
        int idx_res = 0;

        while (cur_round <= max_round) {
            for (idx_y = starty; idx_y < n - cur_round; idx_y++) {
                result[idx_res++] = matrix[startx][idx_y]; 
            }
            for (idx_x = startx; idx_x < m - cur_round; idx_x++) {
                result[idx_res++] = matrix[idx_x][idx_y];
            }
            for (idx_y = n - cur_round; idx_y > starty; idx_y--) {
                result[idx_res++] = matrix[idx_x][idx_y];
            }
            for (idx_x = m - cur_round; idx_x > startx; idx_x--) {
                result[idx_res++] = matrix[idx_x][idx_y];
            }

            cur_round++;
            starty++;
            startx++;
        }

        if (m <= n && m % 2 != 0) {
            for (idx_y = starty; idx_y <= n - cur_round; idx_y++) {
                result[idx_res++] = matrix[startx][idx_y];
            }
        }
        else if (n < m && n % 2 != 0) {
            for (idx_x = startx; idx_x <= m - cur_round; idx_x++) {
                result[idx_res++] = matrix[idx_x][starty];
            }
        }

        return result;
    }
};
```

## Python
```

```
