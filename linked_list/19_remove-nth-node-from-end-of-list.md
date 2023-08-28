# 19. 删除链表的倒数第 N 个结点
[Leetcode](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

## 题目
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

提示:  
* 链表中结点的数目为 sz， 但sz值未知
* 1 <= sz <= 30
* 1 <= n <= sz

## 解法:  
* 双指针法
    * 如果要删除倒数第n个节点，让fast移动 $n+1$ 步，然后让fast和slow同时移动，直到fast指向链表末尾。删掉slow的下一个节点即可。
    * 为什么是fast先移动 $n+1$ 步？因为此时fast和slow之间相差 $n+1$ 个节点，当fast指向链表末尾时，slow指向倒数第 $n+1$ 个节点，即需要删除的节点的前一个节点。这样更方便进行删除操作。

* 性能
    * 时间复杂度: $O(n)$  
    * 空间复杂度: $O(1)$


### C++
```
// 官方解法
// fast先走 n+1 步，然后一直走到 null，此时slow指向倒数第 n+1 个节点，再进行删除操作。
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(-1, head);
        ListNode* slow = dummyHead;
        ListNode* fast = dummyHead;

        // fast先走 n+1 步
        for (int idx = 0; idx <= n; idx++) {
            fast = fast->next;
        }
        
        // fast一直走到 null, 此时slow指向倒数第 n+1 个节点
        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        // 删除倒数第 n 个节点
        ListNode* tmp = slow->next;
        slow->next = tmp->next;
        tmp->next = nullptr;
        delete tmp;
        tmp = nullptr;

        return dummyHead->next;
    }
};
```

```
// 自己的解法
// fast先走 n 步，然后一直走到倒数第一个节点，此时slow指向倒数第 n+1 个节点，再进行删除操作。
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(-1, head);
        ListNode* slow = dummyHead;
        ListNode* fast = dummyHead;
        
        // fast先走 n 步
        while (n--) {
            fast = fast->next;
        }

        // fast一直走到倒数第一个节点，此时slow指向倒数第 n+1 个节点
        while (fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        // 删除倒数第 n 个节点
        ListNode* tmp = slow->next;
        slow->next = tmp->next;
        tmp->next = nullptr;
        delete tmp;
        tmp = nullptr;

        return dummyHead->next;
    }
};
```

### Python
```
# 官方解法
# fast先走 n+1 步，然后一直走到 null，此时slow指向倒数第 n+1 个节点，再进行删除操作。
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        slow = dummyHead
        fast = dummyHead

        for i in range(n + 1):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next

        tmp = slow.next
        slow.next = tmp.next
        
        return dummyHead.next
```

```
# 自己的解法
# fast先走 n 步，然后一直走到倒数第一个节点，此时slow指向倒数第 n+1 个节点，再进行删除操作。
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        slow = dummyHead
        fast = dummyHead

        for i in range(n):
            fast = fast.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        tmp = slow.next
        slow.next = tmp.next
        
        return dummyHead.next
```