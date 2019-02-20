# This is necessary to find the main code
import sys
import heapq
from colorama import Fore, Back

sys.path.insert(0, '../bomberman')
# Import necessary stuff
from entity import CharacterEntity


class TestCharacter(CharacterEntity):
    def __init__(self, name, avatar, x, y):
        CharacterEntity.__init__(self, name, avatar, x, y)
        self.exit = None
        self.bombed = None
        self.tiles = {}
                        
    def do(self, world):   
        if self.exit is None:
            for x in range(world.width()):
                for y in range(world.height()):
                    if world.exit_at(x, y):
                        self.exit = (x, y)
        
        path = get_path(world, (self.x, self.y), self.exit)
        
        self.tiles = {}
        for i in range(1, len(path)):
            self.set_cell_color(path[i][0], path[i][1], Fore.RED + Back.GREEN)
        
        next_cell = path[1]
        if self.bombed is not None:
            if world.bomb_at(self.bombed[0], self.bombed[1]) is None \
                    and world.explosion_at(self.bombed[0], self.bombed[1]) is None:
                self.bombed = None
        elif not world.wall_at(next_cell[0], next_cell[1]):
            self.move(next_cell[0]-self.x, next_cell[1]-self.y)
        else:
            self.place_bomb()
            self.bombed = (self.x, self.y)
            self.move(-1, -1)


# Adapted from RedBlobGames
def get_path(world, start, end):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            break

        for direction in [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1),  (-1, 1), (-1, -1),  (0, 0)]:
            next_cell = (current[0]+direction[0], current[1]+direction[1])
            if next_cell[0] < 0 or next_cell[0] >= world.width() \
                    or next_cell[1] < 0 or next_cell[1] >= world.height():
                continue
            if world.wall_at(next_cell[0], next_cell[1]):
                for dir2 in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (0, 1)]:
                    if world.bomb_at(next_cell[0]+dir2[0], next_cell[1]+dir2[1]):
                        cost = 10
                    else:
                        cost = 10
            elif world.explosion_at(next_cell[0], next_cell[1]):
                cost = 99999999
            elif world.monsters_at(next_cell[0], next_cell[1]):
                cost = 99999999
            elif world.bomb_at(next_cell[0], next_cell[1]):
                cost = 99999999
            else:
                cost = 1

            for dir2 in [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (0, 1)]:
                if world.monsters_at(next_cell[0]+dir2[0], next_cell[1]+dir2[1]):
                    cost = 99999999

            new_cost = cost_so_far[current] + cost
            if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                cost_so_far[next_cell] = new_cost
                priority = new_cost + heuristic(end, next_cell)
                frontier.put(next_cell, priority)
                came_from[next_cell] = current
    current = end
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


def heuristic(a, b):
    # Manhattan distance - minimum number of cells to get from a to b
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


# From RedBlobGames
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
