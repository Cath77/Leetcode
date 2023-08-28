# 25. K 个一组翻转链表
[Leetcode](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

## 题目
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。  
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。   
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

提示:  
* 链表中的节点数目为 n，但 n 具体的值未知。
* 1 <= k <= n <= 5000

## 解法:  
* 由于链表具体长度未知，因此需要从头逐一遍历。在遍历的同时判断是否满足k个一组。
* 如果满足k个一组，记录该组的第一个与最后一个节点，与原链表截断，在使用头插法实现翻转后，再与原链表连接。
* 如果不满足k个一组，直接返回原链表。

性能
* 时间复杂度: $O(n)$  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* dummyHead = new ListNode(-1, head);
        ListNode* pre = dummyHead;
        ListNode* succ;
        ListNode* left = pre->next;
        ListNode* right = left;

        while (right) {
            for (int i = 1; i < k; i++) {
                right = right->next;
                if (right == nullptr) return dummyHead->next;
            }
            succ = right->next;
            pre->next = nullptr;
            right->next = nullptr;

            reverse(left);

            pre->next = right;
            left->next = succ;
            pre = left;
            left = pre->next;
            right = left;
        }
        return dummyHead->next;
    }

    void reverse(ListNode* cur) {
        ListNode* new_head = new ListNode(-1, cur);
        ListNode* next;
        while (cur != nullptr && cur->next != nullptr) {
            next = cur->next;
            cur->next = next->next;
            next->next = new_head->next;
            new_head->next = next;
        }
    }
};
```

## Python
```
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        dummyHead = ListNode(-1, head)
        pre = dummyHead
        succ = pre
        left = pre.next
        right = left

        while right != None:
            for idx in range(1, k):
                right = right.next
                if right == None:
                    return dummyHead.next

            succ = right.next
            pre.next = None
            right.next = None

            self.reverse(left)

            pre.next = right
            left.next = succ

            pre = left
            left = pre.next
            right = left

        return dummyHead.next

    def reverse(self, cur: Optional[ListNode]) -> None:
        new_head = ListNode(-1, cur)
        
        while cur != None and cur.next != None:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = new_head.next
            new_head.next = nxt
        
```
