from Cell import Cell
from AStar import AStar
from Heuristics import Heuristics
import time
width = 6
height = 6
start = (0,0)
walls= [ (1,2), (2,3), (4,3),(5,3)]
end = (5,4)
if __name__ == '__main__':
   
   print("---------A* for maze solve--------\n\n\n")
   limit = int(input("Number of testes->"))
   for x in range(0,limit):
   		print("Insert the number of tests:   "+ str(x))
   		labirinto = AStar()
   		labirinto.init_grid( width, height, walls, start, end)
   		path=labirinto.solve()
   		print(path)
   #print((labirinto.get_cell(4, 0).x))
  		# labirinto.solve()
