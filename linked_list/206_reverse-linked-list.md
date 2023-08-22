# 206. 反转链表
[Leetcode](https://leetcode.cn/problems/reverse-linked-list/)

## 题目
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

## 解法:  

### 迭代法（双指针法）

* 性能
    * 时间复杂度: $O(n)$，其中 n 是链表的长度。需要遍历链表一次  
    * 空间复杂度: $O(1)$。空间复杂度主要取决于递归调用的栈空间，最多为 n 层。


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
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head;
        ListNode* pre = nullptr;
        ListNode* res = reverse(cur, pre);
        return res;
    }

    ListNode* reverse(ListNode* cur, ListNode* pre) {
        if (cur != nullptr) {
            ListNode* tmp = cur->next;
            cur->next = pre;   
            return reverse(tmp, cur);         
        }
        else {
            return pre;
        }
    }
};
```


#### Python
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        return self.reverse(cur, pre)

    def reverse(self, cur, pre):
        if cur != None:
            tmp = cur.next
            cur.next = pre
            return self.reverse(tmp, cur)
        else:
            return pre
```