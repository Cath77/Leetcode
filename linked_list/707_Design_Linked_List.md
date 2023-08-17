# 707. 设计链表
[Leetcode](https://leetcode.cn/problems/design-linked-list/)

## 单链表

### C++
* 在addAtIndex中调用addAtHead与addAtTail
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
```

```
class MyLinkedList {
private:
    int size;
    ListNode* dummyHead;

public:

    // struct ListNode{
    //     int val;
    //     ListNode* next;
    //     ListNode(): val(0), next(nullptr) {}
    //     ListNode(int v): val(v), next(nullptr) {}
    //     ListNode(int v, ListNode* n): val(v), next(n) {}
    // };

    MyLinkedList() {
        size = 0;
        dummyHead = new ListNode(0);
    }
    
    int get(int index) {
        if (index >= size || index < 0) {
            return -1;
        }
        else {
            ListNode* cur_node = dummyHead;
            for (int i = -1; i < index; i++) {
            cur_node = cur_node->next;
            }
            return cur_node->val;
        }
    }
    
    void addAtHead(int val) {
        ListNode* new_node = new ListNode(val, dummyHead->next);
        dummyHead->next = new_node;
        size++;
    }
    
    void addAtTail(int val) {
        ListNode* new_node = new ListNode(val);
        ListNode* cur_node = dummyHead;
        while (cur_node->next != nullptr) {
            cur_node = cur_node->next;
        }
        cur_node->next = new_node;
        size++;
    }
    
    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return;
        }
        else if (index == 0) {
            addAtHead(val);
        }
        else if (index == size) {
            addAtTail(val);
        }
        else {
            ListNode* new_node = new ListNode(val);
            ListNode* cur_node = dummyHead;
            for (int i = -1; i < index - 1; i++) {
                cur_node = cur_node->next;
            }
            new_node->next = cur_node->next;
            cur_node->next= new_node;
            size++;
        }
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        else {
            ListNode* cur_node = dummyHead;
            for (int i = -1; i < index - 1; i++) {
                cur_node = cur_node->next;
            }
            ListNode* tmp = cur_node->next;
            cur_node->next = tmp->next;
            delete tmp;
            tmp = nullptr;
            size--;
        }
    }
};
```


### Python
* 在addAtIndex中调用addAtHead与addAtTail
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
```

```
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            cur_node = self.dummy_head
            for i in range(-1, index):
                cur_node = cur_node.next
            return cur_node.val


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.dummy_head.next)
        self.dummy_head.next = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        cur_node = self.dummy_head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = ListNode(val)
            cur_node = self.dummy_head
            for i in range(-1, index - 1):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        else:
            cur_node = self.dummy_head
            for i in range(-1, index - 1):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
            self.size -= 1
```


## 双链表

### C++
```
struct DListNode {
    int val;
    DListNode* prev;
    DListNode* next;
    DListNode(): val(0), next(nullptr), prev(nullptr) {}
    DListNode(int val): val(val), next(nullptr), prev(nullptr) {}
};

class MyLinkedList {
private:
    int size;
    DListNode* head;
    DListNode* tail;

public:
    MyLinkedList() {
        size = 0;
        head = new DListNode(0);
        tail = new DListNode(0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        else {
            if (index < size / 2) {
                DListNode* cur = head;
                for (int i = -1; i < index; i++) {
                    cur = cur->next;
                }
                return cur->val;
            }
            else {
                DListNode* cur = tail;
                for (int i = size; i > index; i--) {
                    cur = cur->prev;
                }
                return cur->val;
            }
        }
    }
    
    void addAtHead(int val) {
        DListNode* new_node = new DListNode(val);
        new_node->next = head->next;
        head->next->prev = new_node;
        head->next = new_node;
        new_node->prev = head;
        size++;
    }
    
    void addAtTail(int val) {
        DListNode* new_node = new DListNode(val);
        new_node->prev = tail->prev;
        tail->prev->next = new_node;
        tail->prev = new_node;
        new_node->next = tail;
        size++;
    }

    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return;
        }
        else if (index == size) {
            addAtTail(val);
        }
        else if (index == 0) {
            addAtHead(val);
        }
        else {
            if (index < size / 2) {
                DListNode* cur = head;
                DListNode* new_node = new DListNode(val);
                for (int i = -1; i < index - 1; i++) {
                    cur = cur->next;
                }
                new_node->next = cur->next;
                cur->next->prev = new_node;
                cur->next = new_node;
                new_node->prev = cur;
                size++;
            }
            else {
                DListNode* cur = tail;
                DListNode* new_node = new DListNode(val);
                for (int i = size; i > index; i--) {
                    cur = cur->prev;
                }
                new_node->prev = cur->prev;
                cur->prev->next = new_node;
                new_node->next = cur;
                cur->prev = new_node;
                size++;
            }
        }
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        else {
            if (index < size / 2) {
                DListNode* cur = head;
                for (int i = -1; i < index - 1; i++) {
                    cur = cur->next;
                }
                DListNode* tmp = cur->next;
                tmp->next->prev = cur;
                cur->next = tmp->next;
                delete tmp;
                tmp = nullptr;
                size--;
            }
            else {
                DListNode* cur = tail;
                for (int i = size; i > index + 1; i--) {
                    cur = cur->prev;
                }
                DListNode* tmp = cur->prev;
                tmp->prev->next = cur;
                cur->prev = tmp->prev;
                delete tmp;
                tmp = nullptr;
                size--;
            }
        }
    }
};
```


### Python
```
class DListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = DListNode()
        self.tail = DListNode(0, None, self.head)
        self.head.next= self.tail

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            cur = self.head
            for i in range(-1, index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = DListNode(val, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = DListNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            if index < self.size // 2:
                cur = self.head
                for i in range(-1, index - 1):
                    cur = cur.next
                new_node = DListNode(val, cur.next, cur)
                cur.next.prev = new_node
                cur.next = new_node
                self.size += 1
            else:
                cur = self.tail
                for i in range(self.size, index, -1):
                    cur = cur.prev
                new_node = DListNode(val, cur, cur.prev)
                cur.prev.next = new_node
                cur.prev = new_node
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        else:
            if index < self.size // 2:
                cur = self.head
                for i in range(-1, index - 1):
                    cur = cur.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next.prev = cur
                self.size -= 1
            else:
                cur = self.tail
                for i in range(self.size, index + 1, -1):
                    cur = cur.prev
                tmp = cur.prev
                cur.prev = tmp.prev
                tmp.prev.next = cur
                self.size -= 1
```