
from collections import deque
from treenode import TreeNode
from typing import List, Optional, Dict, Deque, Tuple


class IterativeBFS:

    """
    🌳 Reconstructs a binary tree using Iterative Breadth-First Search.

    Uses a queue to process subtree reconstruction tasks level by level.

    Each task maintains:
        - Inorder boundaries of the current subtree.
        - Postorder boundaries of the current subtree.
        - Parent node and the child position to attach.

    An inorder hash map enables efficient root identification,
    while the queue manages pending left and right subtrees.
    """

    @staticmethod
    def buildTree(
        inorder: List[int],
        postorder: List[int]
    ) -> Optional[TreeNode]:

        # 📏 Determine the number of nodes in the binary tree.
        n: int = len(inorder)

        # 🛑 An empty traversal represents an empty binary tree.
        if not n:
            return None

        # 🗺️ Map each node value to its inorder index.
        # This avoids repeated searches when partitioning subtrees.
        inorder_map: Dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }

        # 🌱 The last postorder element identifies the original root.
        root: TreeNode = TreeNode(postorder[n - 1])

        # 📚 Each queue entry represents a subtree reconstruction task:
        # (inorder_start, inorder_end,
        #  postorder_start, postorder_end,
        #  parent_node, is_left_child)
        treeQueue: Deque[Tuple[int, int, int, int, TreeNode, bool]] = deque()

        # ➕ Schedule the root's left and right subtree reconstruction.
        root_index: int = inorder_map[root.val]
        left_tree_size: int = root_index

        # ⬅️ Enqueue the left subtree if it contains any nodes.
        if root_index > 0:
            treeQueue.append((
                0,
                root_index - 1,
                0,
                left_tree_size - 1,
                root,
                True
            ))

        # ➡️ Enqueue the right subtree if it contains any nodes.
        if root_index < n - 1:
            treeQueue.append((
                root_index + 1,
                n - 1,
                left_tree_size,
                n - 2,
                root,
                False
            ))

        # 🔄 Process pending subtree tasks in FIFO order.
        # This ensures reconstruction progresses level by level.
        while treeQueue:

            (
                inorder_start,
                inorder_end,
                postorder_start,
                postorder_end,
                parent,
                is_left
            ) = treeQueue.popleft()

            # 🌱 The final element of the current postorder range
            # identifies the root of this particular subtree.
            root_value: int = postorder[postorder_end]
            node: TreeNode = TreeNode(root_value)

            # 🔗 Attach the newly constructed node to its parent.
            if is_left:
                parent.left = node
            else:
                parent.right = node

            # 🔍 Locate the current root in inorder to divide
            # its traversal range into left and right subtrees.
            index: int = inorder_map[root_value]

            # 📏 Calculate the number of nodes in the left subtree.
            left_tree_size: int = index - inorder_start

            # ⬅️ Schedule the left subtree for reconstruction.
            if left_tree_size > 0:
                treeQueue.append((
                    inorder_start,
                    index - 1,
                    postorder_start,
                    postorder_start + left_tree_size - 1,
                    node,
                    True
                ))

            # ➡️ Schedule the right subtree for reconstruction.
            right_tree_size: int = inorder_end - index

            if right_tree_size > 0:
                treeQueue.append((
                    index + 1,
                    inorder_end,
                    postorder_start + left_tree_size,
                    postorder_end - 1,
                    node,
                    False
                ))

        # 🌳 Return the completely reconstructed binary tree.
        return root
