class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class CircleSingleLinkNode(object):
    # 单向循环链表
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 判空
        return self.__head is None

    def length(self):
        # 链表长度
        if self.is_empty():
            return 0
        else:
            cur = self.__head
            count = 0
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        # 遍历输出
        if self.is_empty():
            print("链表为空!")
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.item, end=" ")
                cur = cur.next
            print(cur.item)

    def add(self,item):
        # 头插法
        # item保存要添加的数值
        node = Node(item)
        # 寻找尾节点
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self,item):
        # 尾插法
        node = Node(item)
        # 如果链表为空，需要特殊处理
        if self.is_empty() is None:
            self.__head=node
            node.next = node
        else:
            cur=self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            # node.next = None

    def insert(self,place,item):
        #指定位置添加元素
        node = Node(item)
        count = 0
        # 头部
        if place <= 0:
            self.add(item)
        # 尾部
        elif place >= self.length():
            self.append(item)
        # 中间
        else:
            cur = self.__head
            while count <= place-1:
                count += 1
                cur = cur.next
            node.next= cur.next
            cur.next=node

    def pop(self,item):
#         删除指定元素
        if self.is_empty():
            pass
        else:
            cur = self.__head
            pre = None
            rear = self.__head
            while cur.next != self.__head:
                # 找到删除元素
                if cur.item == item:
                    # 头部找到元素
                    if cur == self.__head:
                        # 找到尾节点
                        while rear.next != self.__head:
                            rear = rear.next
                        self.__head = cur.next
                        rear.next = self.__head
                    # 其他地方找到元素
                    else:
                        pre.next=cur.next
                # 移动游标
                pre = cur
                cur=cur.next
        #     退出循环指向尾节点
            if cur.item == item:
                if self.length() == 1:
                    self.__head =None
                else:
                    pre.next = self.__head

    def search(self, item):
        # 查找元素是否存在
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head :
            # 找到元素
            if cur.item == item:
                return  True
            cur = cur.next
        if cur.item == item:
            return  True
        return False


if __name__ == '__main__':
    ll = CircleSingleLinkNode()
    ll.is_empty()
    ll.add(100)
    ll.add(200)
    ll.add(300)
    ll.add(400)
    ll.add(500)
    ll.add(600)
    print(ll.length())
    ll.travel()
    ll.insert(2,200)
    ll.travel()
    ll.pop(100)