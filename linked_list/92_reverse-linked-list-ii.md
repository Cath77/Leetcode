# 92. 反转链表 II
[Leetcode](https://leetcode.cn/problems/reverse-linked-list-ii/)

## 题目
给你单链表的头指针 head 和两个索引位置 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


## 解法:  

### 头插法
在需要反转的区间里，每遍历到一个节点，让这个新节点来到反转部分的起始位置。链表只遍历了一次。

性能
* 时间复杂度: $O(n)$  
* 空间复杂度: $O(1)$

#### C++
```
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || head->next == nullptr) return head;
        if (left == right) return head;
        
        // 设置一个虚拟头结点
        ListNode* dummyHead = new ListNode(-1, head);
        // 找到left前一位的节点, 是反转部分与原表的第一个连接点, 设为pre
        ListNode* pre = dummyHead;
        for (int idx = 0; idx < left - 1; idx++) {
            pre = pre->next;
        }
        // 记录需要反转部分的头, 反转后将成为新尾
        ListNode* cur = pre->next;
        ListNode* next;

        // 头插实现部分，每次将next插入到pre后面
        for (int idx = left; idx < right; idx++) {
            // 每次循环最初都更新next，是cur的下一个节点
            next = cur->next;
            // 先将cur的next指向下下个节点，再将next插入到pre后面
            cur->next = next->next;
            next->next = pre->next;
            pre->next = next;
        }

        return dummyHead->next;
    }
};
```

#### Python
```
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None or head.next == None or left == right:
            return head
        else:
            dummyHead = ListNode(-1, head)
            pre = dummyHead
            for idx in range(0, left - 1):
                pre = pre.next
            cur = pre.next

            for idx in range(left, right):
                nxt = cur.next

                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt

            return dummyHead.next
```



### 迭代法

性能
* 时间复杂度: $O(n)$  
* 空间复杂度: $O(1)$


#### C++
```
// 官方解法
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr or head->next == nullptr) return head;
        if (left == right) return head;

        // 插入虚拟头结点，以处理头节点的变化
        ListNode* dummy_head = new ListNode(-1, head);

        // 找到left前一位的节点, 是反转部分与原表的第一个连接点, 设为pre
        ListNode* pre = dummy_head;
        for (int left_idx = 0; left_idx < left - 1; left_idx++) {
            pre = pre->next;
        }
        // 记录需要反转部分的头, 反转后将成为新尾
        ListNode* left_node = pre->next;
        
        // 找到right位的节点, 反转后将成为新头
        ListNode* right_node = left_node;
        for (int right_idx = left; right_idx < right; right_idx++) {
            right_node = right_node->next;
        }
        // 记录下一个节点, 是反转部分与原表的后一个连接点, 设为succ
        ListNode* succ = right_node->next;

        // 将需反转的部分切断, 即将连接部分的next指向nullptr
        pre->next = nullptr;
        right_node->next = nullptr;

        // 反转
        reverseNodes(left_node);
        
        // 将连接部分的next重新指向
        // pre->next 应指向新头, 新尾->next 应指向 succ
        pre->next = right_node;
        left_node->next = succ;

        return dummy_head->next;
    }

    void reverseNodes(ListNode* cur) {
        ListNode* pre = nullptr;
        while (cur != nullptr) {
            ListNode* tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
    }
};
```


```
// 自己的解法
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr or head->next == nullptr) return head;
        if (left == right) return head;

        ListNode* dummy_head = new ListNode(-1, head);
        ListNode* pre = dummy_head;
        for (int left_idx = 0; left_idx < left - 1; left_idx++) {
            pre = pre->next;
        }
        ListNode* left_node = pre->next;
        ListNode* cur_left_node = left_node;
        ListNode* cur_right_node = cur_left_node->next;

        ListNode* tmp;
        for (int right_idx = left + 1; right_idx <= right; right_idx++) {
            tmp = cur_right_node->next;
            cur_right_node->next = cur_left_node;
            cur_left_node = cur_right_node;
            cur_right_node = tmp;
        }
        
        pre->next = cur_left_node;
        left_node->next = tmp;

        return dummy_head->next;
    }
};
```

#### Python
```

```

