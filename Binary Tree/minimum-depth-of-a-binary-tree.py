"""
Given a binary tree, your task is to complete the function minDepth which takes one argument the root of the binary tree and prints the min depth of  binary tree .

          1
       /    \
     2       3
   /        
4       

For the tree above the min depth is 2 ie 1 3

Input:

The task is to complete the method which takes one argument, root of Binary Tree. There are multiple test cases. For each test case, this method will be called individually.

Output:
The output will be an integer denoting the min depth of the binary tree.

Constraints:
1 <=T<= 30
1 <= Number of nodes<= 20
 

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
2
2


There are two test cases.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes.

 """
 
 def minDepth(root):
    # Code here
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minDepth(root.right)+1
    if root.right is None:
        return minDepth(root.left)+1
    return min(minDepth(root.left),minDepth(root.right))+1
