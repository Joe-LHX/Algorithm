class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None


# 链队
class SingleLinkQu(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def put_qu(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def get_qu(self):
        cur = self.__head
        pre = None
        while cur.next is not None:
            pre = cur
            cur = cur.next
        number = cur.item
        pre.next = cur.next
        return number

    def long(self):
        count = 0
        cur = self.__head
        while cur is not None:
            cur = cur.next
            count += 1
        return count


if __name__ == '__main__':
    ll = SingleLinkQu()
    ll.put_qu(6)
    ll.put_qu(5)
    ll.put_qu(4)
    ll.put_qu(6)
    print(ll.long())
    print(ll.get_qu())
    print(ll.get_qu())
    print(ll.get_qu())