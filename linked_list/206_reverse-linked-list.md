# 206. 反转链表
[Leetcode](https://leetcode.cn/problems/reverse-linked-list/)

## 题目
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

## 解法:  

### 迭代法（双指针法）

* 性能
    * 时间复杂度: $O(n)$  
    * 空间复杂度: $O(1)$


#### C++
```
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* tmp;
        ListNode* cur = head;
        ListNode* pre = nullptr;
        while(cur != NULL) {
            tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
};
```

#### Python
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
```



### 递归法

* 性能
    * 时间复杂度: $O(n)$  
    * 空间复杂度: $O(n)$


#### C++
```

```


#### Python
```

```