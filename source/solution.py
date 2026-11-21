from treenode import TreeNode
from typing import List, Optional
from .approaches import RecursiveDFS, IterativeDFS, IterativeBFS

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        recursiveDFS: RecursiveDFS = RecursiveDFS(inorder, postorder)
        iterativeDFS: IterativeDFS = IterativeDFS()
        iterativeBFS: IterativeBFS = IterativeBFS()

        return iterativeBFS.buildTree(inorder, postorder)
        # return iterativeDFS.buildTree(inorder, postorder)
        # return recursiveDFS.buildTree(
        #     inorder_start=0,
        #     inorder_end=len(inorder)-1,
        #     postorder_start=0,
        #     postorder_end=len(postorder)-1
        # )
