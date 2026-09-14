class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_path(self, root, target, path):
        if root is None:
            return False

        path.append(root)
        if root is target:
            return True

        if self.find_path(root.left, target, path):
            return True
        if self.find_path(root.right, target, path):
            return True

        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        path_p, path_q = [], []
        self.find_path(root, p, path_p)
        self.find_path(root, q, path_q)

        answer = None
        for node_p, node_q in zip(path_p, path_q):
            if node_p is not node_q:
                break
            answer = node_p

        return answer


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left
q = root.left.right.right
answer = Solution().lowestCommonAncestor(root, p, q)
print("LCA:", answer.val)
