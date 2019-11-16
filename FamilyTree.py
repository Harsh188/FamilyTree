################################################################
# FamilyTree.py
# Author: Harhsith MohanKumar and Suhas Thalanki
# Date: 11/16/2019
# Version: 1.0
# Description: This program is a model representation of an
#	individuals family tree. It consists of a graph with nodes
#	being faimly member objects and the edges being their
#	relationship between them.
################################################################
from Person import Person

adj_matrix = [[]]			

def fillFamilyConnections(f,matrix):
	list_files = f.readlines()
	for line in list_files:
		con = list(line.split(','))
		for i in range(1,len(con)):
			adj_matrix[i].append(con[i].strip())

def viewGraph(adj_matrix):
	for r in adj_matrix:
		for e in r:
			if isinstance(e, Person):
				print(e.get_name(),end=' ')
			else:
				print(e,end=' ')
		print()

def initializeTree():
	global adj_matrix
	f = open('relationships.csv','r')
	names = list(f.readline().split(','))
	adj_matrix = [[Person(name.strip()) for name in names]]
	for i in range(1,len(names)):
		adj_matrix.append([Person(names[i].strip())])
	fillFamilyConnections(f,adj_matrix)
	viewGraph(adj_matrix)
	f.close()

def numRelationships(n):
	'''
	This method will perform a DFS and determine how many edges
	the node has. The number of edges represents the number of
	direct relationships the memeber has.
	parameter: family member (int)
	return: number of relationships (int)
	'''
	pass

def howRelated(n1,n2):
	'''
	This method will determine how closely related two family
	members are. The higher the number the less related they are
	parameters: n1 - family member 1 (int)
				n2 - family member 2 (int)
	'''
	pass

def analyzeMember():
	node = 5
	node1 = 10
	node2 = 2
	numRelationships(node)
	howRelated(node1,node2)

def main():
	initializeTree()
	analyzeMember()

################################################################
#	Driver Code
################################################################

if __name__ == '__main__':
	main()