
from typing import Self


class Node:
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

    def __len__(self):
        if self.is_leaf():
            return len(self.data)
        left = self.left
        if left and left.is_leaf():
            return len(left)
        elif left:
            return (len(left.left) if left.left else 0  ) \
                 + (len(left.right) if left.right else 0)
        else:
            return 0


    def is_leaf(self):
        return self.left is None and self.right is None

    def concat(self, other: Self) -> Self:
        new_root = Node(data=len(self), left=self, right=other)
        new_root.balance()
        return new_root

    def balance(self):
        pass
