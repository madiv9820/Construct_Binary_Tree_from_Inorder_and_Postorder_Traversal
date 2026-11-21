from treenode import TreeNode
from typing import List, Optional

class IterativeDFS:

    """
    🌳 Reconstructs a binary tree using Iterative Depth-First Search.

    Processes postorder in reverse (Root → Right → Left) and
    uses a stack to keep track of nodes whose child relationships
    are still being reconstructed.

    Inorder is also processed backwards (Right → Root → Left)
    to determine whether the next node belongs to the right or
    left subtree.

    Once a node matches the current inorder value, its right
    subtree is complete, allowing reconstruction to move left.
    """

    @staticmethod
    def buildTree(
        inorder: List[int],
        postorder: List[int]
    ) -> Optional[TreeNode]:

        # 📏 Initialize the number of nodes and an empty root.
        n: int = len(inorder)
        root: Optional[TreeNode] = None

        # 🛑 An empty traversal represents an empty binary tree.
        if n:

            # 🔄 Start both traversals from the end.
            # Reversed postorder: Root → Right → Left.
            # Reversed inorder: Right → Root → Left.
            inorder_index: int = n - 1
            postorder_index: int = n - 2

            # 🌱 The last postorder element is the original tree's root.
            root = TreeNode(postorder[n - 1])

            # 📚 Maintain a stack of nodes whose child relationships
            # are being reconstructed.
            treeStack: List[TreeNode] = [root]

            # 🔁 Process every remaining node in reverse postorder.
            while postorder_index >= 0:

                # 🏗️ Create the next node from the reversed postorder.
                node: TreeNode = TreeNode(postorder[postorder_index])
                postorder_index -= 1

                # ➡️ If the stack's top does not match the current
                # inorder value, the next node belongs to its right.
                if treeStack[-1].val != inorder[inorder_index]:

                    # Attach the new node as the right child and
                    # keep it on the stack for further reconstruction.
                    treeStack[-1].right = node
                    treeStack.append(node)

                else:

                    # 🔍 Find all completed ancestors by matching
                    # stack nodes against the reversed inorder traversal.
                    # Each match means its right subtree is complete.
                    while (
                        treeStack
                        and inorder_index >= 0
                        and treeStack[-1].val == inorder[inorder_index]
                    ):
                        currentNode = treeStack.pop()
                        inorder_index -= 1

                    # ⬅️ The last popped node is where the next
                    # postorder node must be attached as a left child.
                    currentNode.left = node
                    treeStack.append(node)

        # 🌳 Return the fully reconstructed binary tree.
        return root
