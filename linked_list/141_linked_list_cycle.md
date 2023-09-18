# 141. 环形链表
[Leetcode](https://leetcode.cn/problems/linked-list-cycle/)

## 题目
给你一个链表的头节点 head ，判断链表中是否有环。如果链表中存在环 ，则返回 true 。 否则，返回 false 。

提示:  
* 链表中节点的数目范围是 [0, $10^4$]

## 解法:  
* 分别定义 fast 和 slow 指针，从头结点出发。fast指针每次移动两个节点，slow指针每次移动一个节点，如果 fast 和 slow指针在途中相遇 ，说明这个链表有环。

性能
* 时间复杂度: $O(n)$, 其中 n 是链表中的节点数。  
* 空间复杂度: $O(1)$, 只使用了slow和fast两个指针。


## C++
```
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != NULL && fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
```
