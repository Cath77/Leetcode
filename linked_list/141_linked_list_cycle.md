# 141. 环形链表
[Leetcode](https://leetcode.cn/problems/linked-list-cycle/)

## 题目
给你一个链表的头节点 head ，判断链表中是否有环。如果链表中存在环 ，则返回 true 。 否则，返回 false 。

提示:  
* 链表中节点的数目范围是 [0, $10^4$]

## 解法:  

* 方法一：快慢指针法
    * 思路
        * 分别定义 fast 和 slow 指针，从头结点出发。fast指针每次移动两个节点，slow指针每次移动一个节点，如果 fast 和 slow指针在途中相遇 ，说明这个链表有环。
    * 性能
        * 时间复杂度: $O(n)$, 其中 n 是链表中的节点数。  
        * 空间复杂度: $O(1)$, 只使用了slow和fast两个指针。
* 方法二：哈希表
    * 思路
        * 使用哈希表来存储所有已经访问过的节点。
        * 每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表;
        * 否则就将该节点加入哈希表中。重复这一过程，直到遍历完整个链表为止。
    * 性能
        * 时间复杂度：$O(n)$，其中 n 是链表中的节点数。最坏情况下我们需要遍历每个节点一次。
        * 空间复杂度：$O(n)$，其中 n 是链表中的节点数。主要为哈希表的开销，最坏情况下我们需要将每个节点插入到哈希表中一次。

## C++
```
// 方法一：快慢指针法
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

```
// 方法二：哈希表
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> nodes;
        ListNode* tmp = head;
        while (tmp != NULL) {
            if (nodes.contains(tmp)) {
                return true;
            }
            else {
                nodes.emplace(tmp);
                tmp = tmp->next;
            }
        }
        return false;
    }
};
```



## Python
```
# 方法一：快慢指针法
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

```
# 方法二：哈希表
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        tmp = head
        while tmp != None:
            if tmp not in nodes:
                nodes.add(tmp)
                tmp = tmp.next
            else:
                return True
        return False

```