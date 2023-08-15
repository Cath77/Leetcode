# 237. 删除链表中的节点
[Leetcode](https://leetcode.cn/problems/delete-node-in-a-linked-list/)

## 题目
有一个单链表，无法访问第一个节点head，但需要删除的给定节点 node。  
链表的所有值都是 唯一的，并且给定的节点 node 不是链表中的最后一个节点。  
注意，删除节点并不是指从内存中删除它，而是：
* 给定节点的值不应该存在于链表中。
* 链表中的节点数应该减少 1。
* node 前面的所有值顺序相同。
* node 后面的所有值顺序相同。

提示:  
* 链表中节点的数目范围是 [2, 1000]
* -1000 <= Node.val <= 1000
* 链表中每个节点的值都是 唯一 的
* 需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点

## 解法:  
* 和下个节点交换值，然后删除下个节点  
修改node节点的值修改为下个节点的值，并将其指针指向下下个节点

性能
* 时间复杂度: $O(1)$，无需查找，只需删除
* 空间复杂度: $O(1)$


## C++
```
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```

## Python
```
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next
```
