# Definition for singly-linked list.

class Node(object):
    "single link list node"
    def __init__(self, item, next=None) -> None:
        self.item = item
        self.next = next


class SingleLinkList(object):
    "single link list"

    def __init__(self) -> None:
        self._head = None


if __name__ == '__main__':
    link_list = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    link_list._head = node1
    
