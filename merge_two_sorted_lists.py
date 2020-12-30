class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


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
        node = self.head
        while node is not None:
            print(node)
            node = node.next

    def return_head(self):
        return self.head

    def add_head(self, node):
        self.head = node


x = LinkedList()
x.add(1)
x.add(2)
x.add(4)
x.add(5)

y = LinkedList()
y.add(1)
y.add(3)
y.add(4)
y.add(6)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(val=l1.val if l1.val <= l2.val else l2.val)
        node = head
        while l1.next or l2.next is not None:
            if l1.val <= l2.val:
                node.next = l1
            else:
                node.next = l2
            l1 = l1.next
            l2 = l2.next
            node = node.next
        return head


z = LinkedList()
z.add_head(Solution().mergeTwoLists(x.return_head(), y.return_head()))
z.print_list()
