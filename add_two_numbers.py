#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list_node(node):
    print(node.val)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, other):
        if self.head is None:
            self.head = ListNode(other)
            return
        lastbox = self.head
        while lastbox.next:
            lastbox = lastbox.next
        lastbox.next = ListNode(other)

    def print_list(self):
        #print_str = ''
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next
        #print(print_str)

    def return_head(self):
        return self.head

    def add_head(self, node):
        self.head = node


x = LinkedList()
x.add(2)
x.add(4)
x.add(3)

y = LinkedList()
y.add(5)
y.add(6)
y.add(4)


def addTwoNumbers(l1, l2):
    ret = curr = ListNode(0)
    take_away = 0
    while l1 or l2 or take_away:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        total = v1 + v2 + take_away
        take_away = total // 10
        val = total % 10
        curr.next = ListNode(val)
        curr = curr.next
    return ret.next


z = LinkedList()

z.add_head(addTwoNumbers(x.return_head(), y.return_head()))
print(z.print_list())
