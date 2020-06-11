
class ListStrack(object):
    # 顺序栈
    def __init__(self):
        self.item = []

    def is_empty(self):
        # 判空
        return len(self.item) == 0

    def push(self,item):
        # 入栈
        self.item.append(item)

    def pop(self):
        # 出栈
        number = self.item[-1]
        self.item.pop()
        return number

    def peek(self):
        # 返回栈顶
        return self.item[-1]

    def size(self):
        # 栈的大小
        return len(self.item)


if __name__ == "__main__":
    ll = ListStrack()
    ll.push(3)
    ll.push(6)
    ll.push(89)
    print(ll.peek())
    ll.pop()
    print(ll.pop())
    print(ll.pop())