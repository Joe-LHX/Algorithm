class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


# 链栈
class LinkStrack(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        # 判断栈是否为空
        return self.__head is None

    def push(self,item):
        # 入栈
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def pop(self):
        # 出栈
        cur = self.__head
        number = cur.item
        self.__head = cur.next
        return number

    def get_top(self):
        # 取栈顶元素
        if self.is_empty():
            print("该栈为空！")
        else:
            return self.__head.item

    def destroy(self):
        # 销毁栈
       self.__head = None


if __name__ == "__main__":
    ll = LinkStrack()
    ll.push(3)
    ll.push(6)
    ll.push(89)
    print(ll.get_top())
    ll.pop()
    print(ll.pop())
    print(ll.pop())
    ll.destroy()