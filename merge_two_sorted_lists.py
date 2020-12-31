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
x.add(-9)
x.add(3)

y = LinkedList()
y.add(5)
y.add(7)



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode()
        node = head
        while l1 and l2 is not None:
            if l1.val <= l2.val:
                node.val = l1.val
                node.next = l1
                l1 = l1.next
            else:
                node.val = l2.val
                node.next = l2
                l2 = l2.next

            if l1 is None:
                node.next = l2
            elif l2 is None:
                node.next = l1
            else:
                node = node.next

        return head


z = LinkedList()
z.add_head(Solution().mergeTwoLists(x.return_head(), y.return_head()))
z.print_list()
