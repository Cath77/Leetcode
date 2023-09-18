# 142. 环形链表 II
[Leetcode](https://leetcode.cn/problems/linked-list-cycle-ii/)

## 题目
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。  
不允许修改 链表。

提示:  
* 链表中节点的数目范围在范围 $[0, 10^4]$ 内

## 解法:  
* 快慢指针
  * 判断链表是否有环：分别定义 fast 和 slow 指针，从头结点出发。fast指针每次移动两个节点，slow指针每次移动一个节点，如果 fast 和 slow指针在途中相遇 ，说明这个链表有环。
  * 如果有环，如何找到这个环的入口：从头结点出发一个指针，从相遇节点也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点。

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
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None and fast.next.next != None:
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
            slow = head
            while slow != fast:
              slow = slow.next
              fast = fast.next
            return slow
        return None
```
