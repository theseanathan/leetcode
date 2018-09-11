import sys

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def main(args):
    node = Node(value=1)
    node.next = Node(value=2)
    node.next.next = Node(value=3)
    node.next.next.next = Node(value=4)
    node.next.next.next.next = Node(value=5)
    node.next.next.next.next.next = Node(value=6)
    node.next.next.next.next.next.next = Node(value=9)

    node = reverseList(node, node.next)

    """
    print('node: ', node.value)
    print('node.next: ', node.next.value)
    print('node.next.next: ', node.next.next.value)
    """
    cursor = node
    while cursor is not None:
        print(cursor.value)
        cursor = cursor.next

"""
1 -> 2 -> 3 -> 4 -> None
4 -> 3 -> 2 -> 1
"""
def reverseList(node, tail=None):
    if node.next is None:
        return node

    newNode = reverseList(node.next, node.next.next)
    node.next = None

    if newNode.next is None:
        newNode.next = node
    elif tail is not None:
        tail.next = node

    return newNode

if __name__ == "__main__":
   main(sys.argv[1:])
