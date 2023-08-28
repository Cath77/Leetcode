# 24. 两两交换链表中的节点
[Leetcode](https://leetcode.cn/problems/swap-nodes-in-pairs/)

## 题目
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。


## 解法:  
使用虚拟头结点来统一处理头结点变与不变的情况。
使用两个指针来指向需要置换的两个结点。此处类似于头插法，但需要不停更新pre，cur和next的位置。

性能
* 时间复杂度: $O(n)$  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* dummyHead = new ListNode(-1, head);
        ListNode* cur = dummyHead->next;
        ListNode* pre = dummyHead;
        ListNode* next;
        
        while (cur != nullptr && cur->next != nullptr) {            
            // 必须在每个循环开始时更新next
            // 如果在置换后与cur和pre一起更新next，则新cur可能指向空指针，再将next指向cur->next就会出错
            next = cur->next;
            
            cur->next = next->next;
            next->next = cur;
            pre->next = next;

            pre = cur;
            cur = cur->next;
        }

        return dummyHead->next;
    }
};
```

## Python
```
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            dummyHead = ListNode(-1, head)
            pre = dummyHead
            
            while pre.next != None and pre.next.next != None:
                cur = pre.next
                nxt = cur.next

                cur.next = nxt.next
                nxt.next = cur
                pre.next = nxt

                pre = cur

            return dummyHead.next
```
