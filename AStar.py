from Cell import Cell
import time
import random
from Heuristics import Heuristics
def validadePath(node_position,maze):
 # verificar limites
    if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
        return 1
    else:
        return 0    
def isWall(node_position,maze):
    #verifica se é parede
    if (maze[node_position[0]][node_position[1]] != 0):
        return 1
    return 0   

def astar(maze, start, end):
  #usando euclidana
    posicaoRobotinicial = Cell(None, start)
    posicaoRobotinicial.g = posicaoRobotinicial.h = posicaoRobotinicial.f = 0
    point_node = Cell(None, end)
    point_node.g = point_node.h = point_node.f = 0

    #Inicializa lista de abertos e fechados
    closed_list = []
    open_list = []


    open_list.append(posicaoRobotinicial)

    while len(open_list) > 0:

        # pega o no atual, neste caso o primeiro da lista
        nodoAtual = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < nodoAtual.f:
                nodoAtual = item
                current_index = index

        # retira o primeiro e adiciona na lista de fechados
        open_list.pop(current_index)
        closed_list.append(nodoAtual)

        if nodoAtual == point_node:
            path = []
            current = nodoAtual
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Retorna o caminho percorrindo

        # lista de adjacentes
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (nodoAtual.position[0] + new_position[0], nodoAtual.position[1] + new_position[1])

            if validadePath(node_position,maze)==1:
                continue

            # Verifica se  é parede
            if (isWall(node_position,maze)==1):
                continue

            new_node = Cell(nodoAtual, node_position)
            children.append(new_node)

        for child in children:

            # no é inserido na lista de fechados
            for closed_child in closed_list:
                if child == closed_child:
                    break
            heuristics = Heuristics()
            #Utiliza a heuristica desejada que a 
            heuristics.euclidean(child,point_node,nodoAtual)
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

def astar2(maze, start, end):
 #usando manhattan
    posicaoRobotinicial = Cell(None, start)
    posicaoRobotinicial.g = posicaoRobotinicial.h = posicaoRobotinicial.f = 0
    point_node = Cell(None, end)
    point_node.g = point_node.h = point_node.f = 0

    #Inicializa lista de abertos e fechados
    closed_list = []
    open_list = []


    open_list.append(posicaoRobotinicial)

    while len(open_list) > 0:

        # pega o no atual, neste caso o primeiro da lista
        nodoAtual = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < nodoAtual.f:
                nodoAtual = item
                current_index = index

        # retira o primeiro e adiciona na lista de fechados
        open_list.pop(current_index)
        closed_list.append(nodoAtual)

        if nodoAtual == point_node:
            path = []
            current = nodoAtual
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Retorna o caminho percorrindo

        # lista de adjacentes
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (nodoAtual.position[0] + new_position[0], nodoAtual.position[1] + new_position[1])

            if validadePath(node_position,maze)==1:
                continue

            # Verifica se  é parede
            if (isWall(node_position,maze)==1):
                continue

            new_node = Cell(nodoAtual, node_position)
            children.append(new_node)

        for child in children:

            # no é inserido na lista de fechados
            for closed_child in closed_list:
                if child == closed_child:
                    break
            heuristics = Heuristics()
            #Utiliza a heuristica desejada que a 
            heuristics.manhattan(child,point_node,nodoAtual)
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)

def generateMazeRandom(start,end,s,nwalls):
	maze = [[random.randint(0, 0) for x in range(s)] for x in range(s)]
	s=s-1
	for x in range(0,nwalls):
		i = random.randint(0,s)
		j = random.randint(0,s)
		while( start[0] == i and start[1] == j):
			i = random.randint(0,s)
			j = random.randint(0,s)
		while( end[0] == i and end[1] == j):
			i = random.randint(0,s)
			j = random.randint(0,s)
		maze[i][j] = 1;
	
	for x in maze:
		print(x) 
	return maze	
MAZESIZE = 	6	
WALLS = 8

def main():
    mediaTime = 0.0
    mediaLength= 0.0
    limit  = 0
    mazeList = []
    endlist = []
    start = (0, 0)
    mediaLength2= 0.0
    mediaTime2=0.0

    limit = int(input("\nInsert number of tests->>>>>"))
    for n in range(0,limit):
        end = (random.randint(0,MAZESIZE-1), random.randint(0,MAZESIZE-1))
        endlist.append(end)
        print("TARGET =" + str(end))
        maze = generateMazeRandom(start,end,MAZESIZE,WALLS)
        print('\n')
        mazeList.append(maze)
    for n in range(0,limit):
        print("\n\nTEST: " + str(n)+"\n")

        
        begin = time.time()
        path = astar(mazeList[n], start, endlist[n])
        end= time.time()
        if path is None:
            print("no way")
            mediaLength = mediaLength+ 0
        else:
            print("LENGTH OF PATH euclidean= "+ str(len(path)))
            print(path)
            mediaLength = mediaLength + (len(path))
        mediaTime = mediaTime + end-begin
        print("Time euclidean:"+ str(end-begin))
        #manhatam starts
        begin2 = time.time()
        path2 = astar2(mazeList[n], start, endlist[n])
        end2= time.time()
        if path2 is None:
            print("no way")
            mediaLength2 = mediaLength2+ 0
        else:
            print("LENGTH OF PATH= "+ str(len(path2)))
            print(path2)
            mediaLength2 = mediaLength2 + (len(path2))
        mediaTime2 = mediaTime2 + (end2-begin2)
        print("Time:"+ str(end2-begin2))
    print("\n----------------------\n\n\tresults")
    print("mediaTime euclidean :"+str(mediaTime/float(limit)))
    print("media path length  euclidean:"+str(mediaLength/float(limit)))
    print("mediaTime manhattan :"+str(mediaTime2/float(limit)))
    print("media path length  manhattan:"+str(mediaLength2/float(limit)))


if __name__ == '__main__':
    main()