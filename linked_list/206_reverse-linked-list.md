# 206. 反转链表
[Leetcode](https://leetcode.cn/problems/reverse-linked-list/)

## 题目
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

## 解法:  

### 迭代法（双指针法）

* 性能
    * 时间复杂度: $O(n)$，其中 n 是链表的长度。需要遍历链表一次  
    * 空间复杂度: $O(1)$。


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



### 递归法（从前往后反转）

* 性能
    * 时间复杂度: $O(n)$  
    * 空间复杂度: $O(n)$。空间复杂度主要取决于递归调用的栈空间，最多为 n 层。


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


### 递归法（从后往前反转）

* 性能
    * 时间复杂度: $O(n)$  
    * 空间复杂度: $O(n)$

#### C++
```
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr or head->next == nullptr) return head;

        ListNode* new_head = reverseList(head->next);
        /*
            第一轮出栈，head为5，head.next为空，返回5
            第二轮出栈，head为4，head.next为5，执行head.next.next=head也就是5.next=4，
                      把当前节点的子节点的子节点指向当前节点
                      此时链表为1->2->3->4<->5，由于4与5互相指向，所以此处要断开4.next=null
                      此时链表为1->2->3->4<-5
                      返回节点5
            第三轮出栈，head为3，head.next为4，执行head.next.next=head也就是4.next=3，
                      此时链表为1->2->3<->4<-5，由于3与4互相指向，所以此处要断开3.next=null
                      此时链表为1->2->3<-4<-5
                      返回节点5
            第四轮出栈，head为2，head.next为3，执行head.next.next=head也就是3.next=2，
                      此时链表为1->2<->3<-4<-5，由于2与3互相指向，所以此处要断开2.next=null
                      此时链表为1->2<-3<-4<-5
                      返回节点5
            第五轮出栈，head为1，head.next为2，执行head.next.next=head也就是2.next=1，
                      此时链表为1<->2<-3<-4<-5，由于1与2互相指向，所以此处要断开1.next=null
                      此时链表为1<-2<-3<-4<-5
                      返回节点5
            出栈完成，最终头节点5->4->3->2->1
         */

        head->next->next = head;
        head->next = nullptr;
        return new_head;
    }
};
```

#### Python
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head
```