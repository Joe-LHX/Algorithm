# @author:Joe


class ListQu(object):
    # 顺序队
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def put_qu(self,item):
        self.item.append(item)

    def get_qu(self):
        number = self.item[0]
        self.item.pop(0)
        return number

    def long(self):
        return len(self.item)


if __name__ == '__main__':
    ll = ListQu()
    ll.put_qu(6)
    ll.put_qu(5)
    ll.put_qu(4)
    ll.put_qu(6)
    print(ll.long())
    print(ll.get_qu())
    print(ll.get_qu())
    print(ll.get_qu())