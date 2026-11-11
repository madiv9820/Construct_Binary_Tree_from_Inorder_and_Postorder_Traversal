from treenode import TreeNode
from typing import List, Optional, Dict

class RecursiveDFS:
    """
    🌳 Reconstructs a binary tree using Recursive Depth-First Search.

    Uses postorder to identify subtree roots and inorder to
    determine their left and right subtree boundaries.

    An inorder hash map enables constant-time average lookups,
    eliminating repeated searches during reconstruction.
    """

    def __init__(self, inorder: List[int], postorder: List[int]) -> None:

        # 📚 Preserve postorder traversal to identify subtree roots.
        self.__postorder: List[int] = postorder

        # 🗺️ Map each node value to its inorder index for O(1)
        # average-time lookups during subtree partitioning.
        self.__inorder_map: Dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }

    def buildTree(
        self,
        inorder_start: int,
        inorder_end: int,
        postorder_start: int,
        postorder_end: int,
    ) -> Optional[TreeNode]:

        # 🛑 BASE CASE: An empty traversal range means there are
        # no more nodes to construct for the current subtree.
        if inorder_start > inorder_end or postorder_start > postorder_end:
            return None

        # 🌱 ROOT IDENTIFICATION:
        # Postorder follows Left → Right → Root, so its last
        # element identifies the current subtree's root.
        root_value: int = self.__postorder[postorder_end]
        root = TreeNode(root_value)

        # 🔍 Locate the root in inorder to separate its subtrees.
        index: int = self.__inorder_map[root_value]

        # 📏 Count the nodes preceding the root in inorder.
        # These nodes form the entire left subtree.
        left_tree_size: int = index - inorder_start

        # ⬅️ LEFT SUBTREE:
        # Extract exactly left_tree_size nodes from both traversals.
        # Recursively reconstruct them and attach the resulting
        # subtree to the current root's left pointer.
        root.left = self.buildTree(
            inorder_start,
            index - 1,
            postorder_start,
            postorder_start + left_tree_size - 1
        )

        # ➡️ RIGHT SUBTREE:
        # Skip the left subtree and current root to isolate
        # the remaining right subtree traversal ranges.
        # Recursively reconstruct and attach the right subtree.
        root.right = self.buildTree(
            index + 1,
            inorder_end,
            postorder_start + left_tree_size,
            postorder_end - 1
        )

        # 🏗️ Return the completed subtree to its parent call.
        return root
