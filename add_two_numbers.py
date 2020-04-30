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
    int1 = 0
    d = 1
    node = l1
    while node:
        int1 += node.val*d
        d = d*10
        node = node.next
    #print(ch1)

    int2 = 0
    d = 1
    node = l2
    while node:
        int2 += node.val * d
        d = d * 10
        node = node.next
    #print(ch2)
    result_int = int1 + int2
    temp = result_int % 10
    lastbox = ListNode(temp)

    temp = result_int

    while temp > 1:
        if temp < 10:
            #node = ListNode(temp)

            node = ListNode(temp)
            lastbox.next = node

        else:
            lastbox.next = ListNode(temp % 10)

        temp = temp // 10

    return lastbox


z = LinkedList()

z.add_head(addTwoNumbers(x.return_head(), y.return_head()))
print(z.print_list())