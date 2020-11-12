class Node:
	def __init__(self, key):
		self.key = key
		self.right = None
		self.left = None

class DAGNode:
	def __init__(self, key):
		self.key = key
		self.parents = []
		self.children = []
		self.distance = None



def findPath( root, path, k): 

	if root is None:
		return False

	path.append(root.key) 

	if root.key == k: 
		return True

	if ((root.left != None and findPath(root.left, path, k)) or (root.right!= None and findPath(root.right, path, k))): 
		return True 

	path.pop() 
	return False

def findLCA(root, n1, n2): 

	path1 = [] 
	path2 = [] 

	if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
		return -1 

	i = 0 
	while (i < len(path1) and i < len(path2)): 
		if path1[i] != path2[i]: 
			break
		i += 1
	return path1[i-1] 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
  
#print("LCA(4, 5) = %d" %(findLCA(root, 4, 5))) 
#print("LCA(4, 6) = %d" %(findLCA(root, 4, 6))) 
#print("LCA(3, 4) = %d" %(findLCA(root, 3, 4))) 
#print("LCA(2, 4) = %d" %(findLCA(root, 2, 4))) 

def findAncestors(root, ancestors, distance):

	if root is None:
		return

	for i in range(len(root.parents)):
		root.parents[i].distance = distance
		ancestors.append(root.parents[i])
		findAncestors(root.parents[i], ancestors, distance + 1)
	

def findDAGLCA(root, n1, n2): 

	if root is None:
		return -1

	n1Ancestors = []
	n2Ancestors = []

	findAncestors(n1, n1Ancestors, 1)
	findAncestors(n2, n2Ancestors, 1)

	commonAncestors = []

	for i in range(len(n1Ancestors)):
		print("Key:", n1Ancestors[i].key)
		print("Distance:", n1Ancestors[i].distance)
		for j in range(len(n2Ancestors)):
			if (n1Ancestors[i].key == n2Ancestors[j].key):
				commonAncestors.append(n1Ancestors[i])
	
	lowestCommonAncestor = commonAncestors[0]

	print("Common Ancestors:")

	for i in range(len(commonAncestors)):
		print(commonAncestors[i].key)
		if (lowestCommonAncestor.distance > commonAncestors[i].distance):
			lowestCommonAncestor = commonAncestors[i]
	
	print(lowestCommonAncestor.key)

	return lowestCommonAncestor.key