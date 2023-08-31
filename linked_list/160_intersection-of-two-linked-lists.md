# 160. 链表相交
[Leetcode](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

## 题目
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。  
题目数据 **保证** 整个链式结构中不存在环。  
注意，函数返回结果后，链表必须 保持其原始结构 。

提示:  
* listA 中节点数目为 m
* listB 中节点数目为 n
* 1 <= m, n <= $3 * 10^4$

## 解法:  
* 求出两个链表的长度，并求出两个链表长度的差值，然后让curA移动到，和curB 末尾对齐的位置.  
* 比较curA和curB是否相同，如果不相同，同时向后移动curA和curB，如果相同，则找到交点。
  * 注意：交点不是数值相等，而是指针相等，即curA == curB。
* 如果遍历到表尾仍未找到焦点，则返回空指针。

性能
* 时间复杂度: $O(m + n)$，其中m和n分别是两个链表的长度  
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA;
        int len_A = 0;
        while (curA != nullptr) {
            curA = curA->next;
            len_A++;
        }

        ListNode* curB = headB;
        int len_B = 0;
        while (curB != nullptr) {
            curB = curB->next;
            len_B++;
        }
        
        curA = headA;
        curB = headB;
        int len_gap = 0;
        if (len_A > len_B) {
            len_gap = len_A - len_B;
            while(len_gap--) {
                curA = curA->next;
            }
        }
        else {
            len_gap = len_B - len_A;
            while (len_gap--) {
                curB = curB->next;
            }
        }

        while (curA != nullptr) {
            if (curA != curB) {
                curA = curA->next;
                curB = curB->next;
            }
            else {
                return curA;
            }
        }

        return NULL;
    }
};
```

## Python
```
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        lenA = 0
        while curA != None:
            curA = curA.next
            lenA += 1

        curB = headB
        lenB = 0
        while curB != None:
            curB = curB.next
            lenB += 1

        curA = headA
        curB = headB
        len_gap = 0
        if lenA > lenB:
            len_gap = lenA - lenB
            for i in range(len_gap, 0, -1):
                curA = curA.next
        else:
            len_gap = lenB - lenA
            for i in range(len_gap, 0, -1):
                curB = curB.next

        while curA != None:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next

        return None
```
