# 59.螺旋矩阵II

## Python
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