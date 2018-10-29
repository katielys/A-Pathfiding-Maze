from Cell import Cell
import time
import random
from Heuristics import Heuristics
def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    # Create start and end node
    start_node = Cell(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Cell(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    #open_list = []
    open_list = set()
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Cell(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            heuristics = Heuristics()
            # Create the f, g, and h values
            heuristics.manhattan(child,end_node,current_node)
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)

def generateMazeRandom(start,end,s,nwalls):
	maze = [[random.randint(0, 0) for x in range(s)] for x in range(s)]
	#print(maze)
	s=s-1
	for x in range(0,nwalls):
		i = random.randint(0,s)
		j = random.randint(0,s)
		if start[0] == i and start[1] == j:
			i = random.randint(0,s)
			j = random.randint(0,s)
		if end[0] == i and end[1] == j:
			i = random.randint(0,s)
			j = random.randint(0,s)
		maze[i][j] = 1;
	#maze[end[0]][end[1]] = 66
	for x in maze:
		print(x) 
	return maze	
		
def main():
	media = 0.0
	limit = int(input("Insert number of tests->>>>>"))
	for n in range(0,limit):
		print("\n\nTEST: " + str(n)+"\n")
		start = (0, 0)
		print("START="+ str(start))
		end = (random.randint(0,6), random.randint(0,6))
		print("END="+ str(end))
		maze = generateMazeRandom(start,end,6,5)
		begin = time.time()
		path = astar(maze, start, end)
		end= time.time()
		print(path)
		media = media + end-begin
		print("Time:"+ str(end-begin))
	print("\n\nMEDIA :"+str(media/limit))

if __name__ == '__main__':
    main()