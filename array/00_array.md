# 数组

## 基础理论

* 存放在**连续内存空间**上的相同类型数据的集合  
因为数组在内存空间的地址是连续的，所以在删除或者增添元素的时候，要移动后续其他元素的地址  
C++数组地址调用(16进制H)：`&array[][]`
* 数组size固定，元素不能删除，只能覆盖



## 704.二分查找 -> 二分法

### 定义
把数组的所有元素从中间一分为二，将要查找的元素跟中间元素的大小进行对比，以此判断要查找的元素在哪一段数组中，使得每次查询便能将数组的查询范围缩短一半。

### 前提
数组为有序数组，且数组中无重复元素  
只要看到面试题里给出的数组是有序数组，都可以想一想是否可以使用二分法

### 性能
* 时间复杂度：O(log n)
* 空间复杂度：O(1)

### 例题
[704_二分法](./704_binary_search.md)

* **左闭右闭`[left, right]`**  $\sqrt{}$  
```
while (left <= right) {
    ...
    if (nums[middle] > target) {
        right = middle - 1;
    }
    ...
}
```
* 左闭右开`[left, right)`
```
while (left < right) {
    ...
    if (nums[middle] > target) {
        right = middle;
    }
}
```

[35_搜索插入位置](./35_search_insert_position.md)  
[34_在排序数组中查找元素的第一个和最后一个位置](./34_find-first-and-last-position-of-element-in-sorted-array.md)  
[69_x的平方根](./69_sqrtx.md)  
[367_有效的完全平方数](./367_valid-perfect-square.md)



## 27. 移除元素 -> 双指针法

### 定义
给一个数组 nums 和一个值 val，需要**原地**移除所有数值等于 val 的元素，并返回移除后数组的**新长度**。  
不要使用额外的数组空间，你必须**仅使用 O(1) 额外空间并原地修改输入数组**。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。  
提示：  
0 <= nums.length <= 100  
0 <= nums[i] <= 50  
0 <= val <= 100

### 注意
数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖

### 例题
[27.移除元素](./27_remove_element.md)

* **双向指针法**  $\sqrt{}$  
时间复杂度: O(n)  
空间复杂度: O(1)

* 快慢指针法  
时间复杂度: O(n)  
空间复杂度: O(1)

* 暴力解法  
时间复杂度: O(n^2)  
空间复杂度: O(1)

[26_删除排序数组中的重复项](./26_remove-duplicates-from-sorted-array.md)  
[283_移动零](./283_move-zeroes.md)  
[844_比较含退格的字符串](./844_backspace-string-compare.md)  
[977.有序数组的平方](./977_Squares_of_a_Sorted_Array.md)




## 977.有序数组的平方 -> 双指针法

### 定义
给一个按**非递减顺序**排序的整数数组 nums，返回**每个数字的平方**组成的新数组，要求也按**非递减顺序**排序。设计时间复杂度为 O(n) 的算法解决本问题。  
提示：  
1 <= nums.length <= 104  
-104 <= nums[i] <= 104  
nums已按非递减顺序排序

### 例题
[977.有序数组的平方](./977_Squares_of_a_Sorted_Array.md)  


* **双指针法**  $\sqrt{}$  
时间复杂度: O(n)   
空间复杂度: O(n)  
数组其实是有序的， 只不过负数平方之后可能成为最大数了。那么数组平方的最大值就在数组的两端，不是最左边就是最右边，不可能是中间。  
此时可以考虑双指针法了，i指向起始位置，j指向终止位置。同时定义一个和原数组一样大小的新数组，从终止位置开始赋值。

[88.合并两个有序数组](./88_merge-sorted-array.md)


## 209.长度最小的子数组 -> 滑动窗口

### 定义
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的**连续子数组**，并返回其长度。如果不存在符合条件的子数组，返回 0。  
提示：  
1 <= target <= 10^9  
1 <= nums.length <= 10^5  
1 <= nums[i] <= 10^5

### 例题
[209.长度最小的子数组](./209_Minimum_Size_Subarray_Sum.md)

* **滑动窗口**  $\sqrt{}$   
时间复杂度：O(n)  
空间复杂度：O(1)

[904_水果成篮（哈希表）](../hash_table//904_fruit-into-baskets.md)  
[76_最小覆盖子串](../hash_table/76_minimum-window-substring.md)  

## 59.螺旋矩阵II -> 模拟法

### 定义
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。  
提示：  
1 <= n <= 20

### 例题
[59.螺旋矩阵II](./59_Spiral_Matrix_II.md)

* **模拟法**  $\sqrt{}$  
模拟顺时针画矩阵的过程:  
填充上行从左到右  
填充右列从上到下  
填充下行从右到左  
填充左列从下到上  
由外向内一圈一圈这么画下去。  
每画一条边都要坚持**一致的左闭右开**，或者**左开右闭**的原则，这样这一圈才能按照统一的规则画下来。  
  
时间复杂度 O(n^2): 矩阵中的每个数都被遍历一次  
空间复杂度 O(n^2): 矩阵的空间占用
 
[54.螺旋矩阵](./54_spiral-matrix.md) 


## 总结
![总结](https://camo.githubusercontent.com/97d746e877876898e216a451d20a4abd607a8ab20f31886a4ab7379fb7cd2214/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f2545362539352542302545372542422538342545362538302542422545372542422539332e706e67)