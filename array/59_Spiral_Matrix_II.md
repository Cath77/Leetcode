# 59.螺旋矩阵II
[Leetcode](https://leetcode.cn/problems/spiral-matrix-ii/)

## Python
```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx = 0
        starty = 0
        max_round = n // 2
        cur_round = 1
        value = 1

        nums = [[0 for i in range(n)] for i in range(n)]

        while cur_round <= max_round:
            for j in range(starty, n - cur_round):
                nums[startx][j] = value
                value += 1
            for i in range(startx, n - cur_round):
                nums[i][n - cur_round] = value
                value += 1
            for j in range(n - cur_round, starty, -1):
                nums[n - cur_round][j] = value
                value += 1
            for i in range(n - cur_round, startx, -1):
                nums[i][starty] = value
                value += 1

            cur_round += 1
            startx += 1
            starty += 1

        if n % 2:
            nums[startx][starty] = value

        return nums
```

```
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1   # 计数
        startx, starty = 0, 0   # 起始位置
        midx, midy = n//2, n//2 # 中心位置
        nums = [[0] * n for _ in range (n)] # 初始化矩阵

        for offset in range(1, midx + 1):
            for i in range(starty, n - offset): # 上边
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset): # 右边
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1): # 下边
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1): # 左边
                nums[i][starty] = count
                count += 1
            startx += 1 # 一圈结束，起始位置向内移动一位
            starty += 1 # 一圈结束，起始位置向内移动一位
        
        if (n % 2) != 0:    # 如果n为奇数，需要单独给矩阵中心赋值
            nums[midx][midy] = count
        
        return nums
```

## C++
```
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> nums(n, vector<int>(n, 0));
        int startx = 0, starty = 0;
        int i, j;
        int value = 1;
        int cur_round = 1;
        int max_round = n / 2;

        while (cur_round <= max_round) {
            for (j = starty; j < n - cur_round; j++) {
                nums[startx][j] = value++;
            }
            for (i = startx; i < n - cur_round; i++) {
                nums[i][j] = value++;
            }
            for (; j > starty; j--) {
                nums[i][j] = value++;
            }
            for (; i > startx; i--) {
                nums[i][j] = value++;
            }

            cur_round++;
            startx++;
            starty++;
        }

        if (n % 2 != 0) {
            nums[startx][starty] = value;
        }

        return nums;        
    }
};
```

```
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> nums(n, vector<int>(n, 0));
        /* Create a 2D vector containing "n" elements each having the value "vector<int> (n, 0)".
        "vector<int> (n, 0)" means a vector having "n" elements each of value "0". */
        int startx = 0, starty = 0;
        int midx = n / 2, midy = n / 2;
        int count = 1;
        for (int offset = 1; offset <= midx; offset++) {
            for (int i = starty; i < n - offset; i++) {
                nums[startx][i] = count++;
            }
            for (int i = startx; i < n- offset; i++) {
                nums[i][n - offset] = count++;
            }
            for (int i = n - offset; i > starty; i--) {
                nums[n - offset][i] = count++;
            }
            for (int i = n - offset; i > startx; i--) {
                nums[i][starty] = count++;
            }
            startx++;
            starty++;
        }
        if (n % 2 != 0) {
            nums[midx][midy] = count;
        }

        return nums;
    }
};
```