import pytest
from lowest_common_ancestor import *

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

	def test_DAG2(self):

		root = DAGNode(0)
		node1 = DAGNode(1)
		node2 = DAGNode(2)
		node3 = DAGNode(3)
		node4 = DAGNode(4)
		node5 = DAGNode(5)
		node6 = DAGNode(6)
		node7 = DAGNode(7)
		node8 = DAGNode(8)
		node9 = DAGNode(9)

		root.children = [node1, node2]
		node1.children = [node3, node4]
		node1.parents = [root]
		node2.children = [node3, node4, node5, node6]
		node2.parents = [root]
		node3.parents = [node1, node2]
		node4.parents = [node1, node2]
		node5.children = [node8]
		node5.parents = [node2]
		node6.children = [node7, node8, node9]
		node6.parents = [node2]
		node7.children = [node9]
		node7.parents = [node6]
		node8.parents = [node5, node6]
		node9.parents = [node6, node7]
		
		lca = findDAGLCA(root, node1, node2)
		
		assert lca == 0

		lca = findDAGLCA(root, node8, node9)
		
		assert lca == 6

		lca = findDAGLCA(root, node5, node9)
		
		assert lca == 2

		lca = findDAGLCA(root, node7, node8)
		
		assert lca == 6

	def test_null(self):

		root = None

		LCA = findLCA(root, 4, 5)

		assert LCA == -1

	
