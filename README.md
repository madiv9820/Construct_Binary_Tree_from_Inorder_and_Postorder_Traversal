# [🌳 Rebuild the Tree: From Inorder to Postorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150)

### 📖 The Story
Imagine you're given two different records of a once-complete family tree. One records everyone by visiting the left branch first, then the parent, and finally the right branch. The other records them by visiting both branches before recording the parent.

The tree itself is missing, but these two traversal records hold all the clues needed to bring it back to life! 🧩

### 🎯 Problem Explanation
You are given two integer arrays, `inorder` and `postorder`, representing the **inorder** and **postorder** traversals of the same binary tree.

Your task is to reconstruct the original binary tree using these two traversal sequences and return its root.

Remember:
- **Inorder:** Left → Root → Right
- **Postorder:** Left → Right → Root
Each value is unique, making it possible to identify every node and determine its correct position in the tree.

#### 🧪 Examples
- **A Complete Tree Reconstruction 🌲**
    - **Input:** <br>
        ![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
        ```
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        ```
    - **Output:** ```[3, 9, 20, None, None, 15, 7]```
- **A Single-Node Tree 🌱**
    - **Input:**
        ```
        inorder = [-1]
        postorder = [-1]
        ```
    - **Output:** ```[-1]```

#### 📌 Constraints
- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- Both arrays contain **unique** values.
- Every value in `postorder` also exists in `inorder`.
- Both arrays are guaranteed to represent valid traversals of the same binary tree.

---