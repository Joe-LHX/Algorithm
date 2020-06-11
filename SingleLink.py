class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None


class SingleLinkNode(object):
    # 单链表
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        # 判空
        return self.__head is None

    def length(self):
        # 链表长度
        cur = self.__head
        count = 0
        while cur is not None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        # 遍历输出
        cur = self.__head
        while cur is not None:
            print(cur.item,end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        # 头插法
        # item保存要添加的数值
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 尾插法
        node = Node(item)
        # 如果链表为空，需要特殊处理
        if self.is_empty() is None:
            self.__head=node
        else:
            cur=self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            # node.next = None

    def insert(self, place, item):
        # 指定位置添加元素
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
        #  删除指定元素
        cur = self.__head
        pre = None
        while cur is not None:
            # 找到删除元素
            if cur.item == item:
                # 头部找到元素
                if cur == self.__head:
                    self.__head = cur.next
                # 其他地方找到元素
                else:
                    pre.next=cur.next
            # 移动游标
            pre = cur
            cur=cur.next

    def search(self,item):
        # 查找元素是否存在
        cur = self.__head
        while cur is not None:
            # 找到元素
            if cur.item == item:
                return  True
            cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleLinkNode()
    ll.is_empty()
    ll.add(100)
    print(ll.length())
    ll.travel()
    ll.insert(2,200)
    ll.travel()
    ll.pop(100)