from typing import Optional

class TreeNode:
    """
    🌳 Represents a single node in a binary tree.

    Each node stores an integer value and maintains references
    to its left and right child nodes.
    """
    
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        # 📦 Store the value carried by the current node.
        self.val: int = val
        
        # ⬅️ Reference to the left child; None if no left child exists.
        self.left: Optional[TreeNode] = left

        # ➡️ Reference to the right child; None if no right child exists.
        self.right: Optional[TreeNode] = right
