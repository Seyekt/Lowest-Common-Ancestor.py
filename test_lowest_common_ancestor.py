import pytest
from lowest_common_ancestor import findLCA, Node

class Test_LCA:

	def test_findLCA(self):
		root = Node(1) 
		root.left = Node(2) 
		root.right = Node(3) 
		root.left.left = Node(4) 
		root.left.right = Node(5) 
		root.right.left = Node(6) 
		root.right.right = Node(7)

		LCA = findLCA(root, 4, 5)
		LCA2 = findLCA(root, 4, 6)

		assert LCA == 2
		assert LCA2 == 1

