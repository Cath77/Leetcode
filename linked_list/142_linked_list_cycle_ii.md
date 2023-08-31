# 142. 环形链表 II
[Leetcode](https://leetcode.cn/problems/linked-list-cycle-ii/)

## 题目
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。  
不允许修改 链表。

提示:  
* 链表中节点的数目范围在范围 $[0, 10^4]$ 内

## 解法:  
* 快慢指针
  * 

性能
* 时间复杂度: $O(n)$。在最初判断快慢指针是否相遇时，slow 指针走过的距离不会超过链表的总长度；随后寻找入环点时，走过的距离也不会超过链表的总长度。因此，总的执行时间为 $O(N)+O(N)=O(N)$。  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != NULL && fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                ListNode* index1 = fast;
                ListNode* index2 = head;
                while (index1 != index2) {
                    index1 = index1->next;
                    index2 = index2->next;
                }
                return index1;
            }
        }
        return NULL;
    }
};
```

## Python
```

```
