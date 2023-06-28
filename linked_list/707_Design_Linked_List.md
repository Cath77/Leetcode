# 707. 设计链表


## 题目
* 实现 MyLinkedList 类：
  * ```MyLinkedList()```: 初始化 MyLinkedList 对象。
  * ```int get(int index)```：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
  * ```void addAtHead(int val)```：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
  * ```void addAtTail(int val)```：将值为 val 的节点追加到链表的最后一个元素。
  * ```void addAtIndex(int index, int val)```：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。
  * ```void deleteAtIndex(int index)```：如果索引 index 有效，则删除链表中的第 index 个节点。


## 性能
* 时间复杂度: 涉及 index 的相关操作为 $O(index)$, 其余为 $O(1)$
* 空间复杂度: $O(n)$


## C++
* 单链表：在addAtIndex中调用addAtHead与addAtTail
```
class MyLinkedList {
public:
    struct LinkedNode {
        int val;
        LinkedNode* next;
        LinkedNode(int x) : val(x), next(nullptr) {}
    };

    // 初始化链表
    MyLinkedList() {
        dummyHead = new LinkedNode(0);  // 虚拟头结点
        size = 0;
    }
    
    // 获取链表中第 index 个节点的值。如果索引无效，则返回-1
    int get(int index) {
        if (index > (size - 1) || index < 0) {
            return -1;
        }
        else {
            LinkedNode* cur = dummyHead;
            // runs the loop until index is 0
            while (index--) {
                cur = cur->next;
            }
            return cur->next->val;
        }
    }
    
    // 在链表的第一个元素之前添加一个值为 val 的节点
    // 插入后，新节点将成为链表的第一个节点
    void addAtHead(int val) {
        LinkedNode* newNode = new LinkedNode(val);
        newNode->next = dummyHead->next;
        dummyHead->next = newNode;
        size ++;
    }
    
    // 将值为 val 的节点追加到链表的最后一个元素
    void addAtTail(int val) {
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = dummyHead;
        while(cur->next != nullptr) {
            cur = cur->next;
        }
        cur->next = newNode;
        size++;
    }
    
    // 在链表中的第 index 个节点之前添加值为 val 的节点
    // 如果 index 等于链表的长度，则该节点将附加到链表的末尾
    // 如果 index 大于链表长度，则不会插入节点
    // 如果index小于0，则在头部插入节点
    void addAtIndex(int index, int val) {
        if(index < 0 or index > size) {
            return;
        }
        else if(index == 0) {
            addAtHead(val);
        }
        else if(index == size) {
            addAtTail(val);
        }
        else {
            LinkedNode* newNode = new LinkedNode(val);
            LinkedNode* cur = dummyHead;
            while(index--) {
                cur = cur->next;
            }
            newNode->next = cur->next;
            cur->next = newNode;
            size++;
        }
    }
    
    // 如果索引 index 有效，则删除链表中的第 index 个节点
    void deleteAtIndex(int index) {
        if (index < 0 || index > (size - 1)) {
            return;
        }
        else {
            LinkedNode* cur = dummyHead;
            while(index--) {
                cur = cur->next;
            }
            LinkedNode* tmp = cur->next;
            cur->next = tmp->next;
            //delete命令指示释放了tmp指针原本所指的那部分内存，
            //被delete后的指针tmp的值（地址）并非就是NULL，而是随机值。也就是被delete后，
            //如果不再加上一句tmp=nullptr,tmp会成为乱指的野指针
            //如果之后的程序不小心使用了tmp，会指向难以预想的内存空间
            delete tmp;
            tmp = nullptr;
            size--;
        }
    }
private:
    LinkedNode* dummyHead;
    int size;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```


## Python
* 单链表：在addAtIndex中调用addAtHead与addAtTail
```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            current = self.dummy_head
            while index > 0:
                current = current.next
                index -= 1
            return current.next.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next != None:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.dummy_head
            while index > 0:
                current = current.next
                index -= 1
            current.next = ListNode(val, current.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        else:
            current = self.dummy_head
            while index > 0:
                current = current.next
                index -= 1
            current.next = current.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```