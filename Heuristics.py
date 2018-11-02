from Cell import Cell
class Heuristics(object):
	def __init__(self):
		pass
	def euclidean(self,child,end_node,current_node):
		child.g = current_node.g 
		child.h =  (((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))**(1/2)
		child.f = child.g + child.h
	def manhattan(self,child,end_node,current_node):
		child.g = current_node.g
		child.h =  (abs((child.position[0] - end_node.position[0]) ) + abs((child.position[1] - end_node.position[1]) ))
		child.f = child.g + child.h