

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root, p):
        successor = None

        while root is not None:
            if p.val >= root.val:
                # p is not smaller, so the answer must be on the right.
                root = root.right
            else:
                # This node can be the answer; look left for a closer one.
                successor = root
                root = root.left

        return successor


def insert(root, value):
    """Insert a value into the BST."""
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def find_node(root, value):
    """Find and return the node with the given value."""
    while root is not None:
        if root.val == value:
            return root
        root = root.left if value < root.val else root.right

    return None


if __name__ == "__main__":
    values = input("Enter BST values separated by commas: ")
    values = [int(value.strip()) for value in values.split(",") if value.strip()]
    target_value = int(input("Enter the value of p: "))

    if not values:
        print("Please enter at least one BST value.")
        exit()

    root = None
    for value in values:
        root = insert(root, value)

    target = find_node(root, target_value)
    if target is None:
        print("The value of p is not present in the BST.")
        exit()

    successor = Solution().inorderSuccessor(root, target)

    if successor is None:
        print("Inorder successor: None")
    else:
        print("Inorder successor:", successor.val)
