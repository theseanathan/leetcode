class Node:
    left = None
    right = None
    val = 0

    def __init__(self, val):
        self.val = val


class MaxEvenSum:
    max_even = 0

    def max_even_sum(self, node):
        if node is None:
            return 0, 0
        if node.left is None and node.right is None:
            return (node.val, 0) if node.val % 2 == 0 else (0, node.val)

        left_even, left_odd = self.max_even_sum(node.left)
        right_even, right_odd = self.max_even_sum(node.right)

        if node.val % 2 == 0:
            odd = max(max(node.val + left_odd, node.val + right_odd), 0)
            even = max(max(node.val + left_even, node.val + right_even), node.val)
            if (node.val + left_even + right_even) % 2 == 0:
                self.max_even = max(self.max_even, node.val + left_even + right_even)
            if (node.val + left_odd + right_odd) % 2 == 0:
                self.max_even = max(self.max_even, node.val + left_odd + right_odd)
        else:
            odd = max(max(node.val + left_even, node.val + right_even), node.val)
            even = max(max(node.val + left_odd, node.val + right_odd), 0)
            if (node.val + left_even + right_odd) % 2 == 0:
                self.max_even = max(self.max_even, node.val + left_even + right_odd)
            if (node.val + left_odd + right_even) % 2 == 0:
                self.max_even = max(self.max_even, node.val + left_odd + right_even)

        if even % 2 == 0:
            self.max_even = max(self.max_even, even)

        return odd, even

    def get_max_even_sum(self, node):
        self.max_even_sum(node)
        return self.max_even


def test():
    node = Node(10)

    node.left = Node(2)
    node.left.left = Node(1)
    node.left.right = Node(101)

    node.right = Node(5)
    node.right.right = Node(13)

    M_sum = MaxEvenSum()
    print(M_sum.get_max_even_sum(node))


if __name__ == "__main__":
    test()
