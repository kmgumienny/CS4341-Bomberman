import math
import sys
sys.path.insert(0, '../bomberman')

from world_utilities import *
from sensed_world import SensedWorld


# 1/(distance to closest exit)^2
def f_to_exit(world, character):
    character_location = (character.x, character.y)

    exits = find_exits(world)

    if len(exits) == 0:
        return 0

    closest_exit = closest_point(character_location, exits, euclidean=False)

    a_star_distance = a_star(world, character_location, closest_exit)[1]+1

    return (1/float(a_star_distance))**2


# 1/(distance to closest monster)^2
def f_to_monster(world, character):
    character_location = (character.x, character.y)

    monsters = find_monsters(world)

    if len(monsters) == 0:
        return 0

    closest_monster = closest_point(character_location, monsters, euclidean=False)

    a_star_distance = a_star(world, character_location, closest_monster)[1]+1

    return (1/float(a_star_distance))**2


# 1/(distance to closest bomb)^2
def f_to_bomb(world, character):
    character_location = (character.x, character.y)

    bombs = find_bombs(world)

    if len(bombs) == 0:
        return 0

    closest_bomb = closest_point(character_location, bombs, euclidean=False)

    a_star_distance = a_star(world, character_location, closest_bomb)[1]+1

    return (1/float(a_star_distance))**2


def f_wall_to_bomb(world, character = None):
    walls = find_walls(world)
    bombs = find_bombs(world)

    if len(bombs) == 0 or len(walls) == 0:
        return 0

    closest_wall = closest_point(bombs[0], walls, euclidean=False)

    a_star_distance = a_star(world, bombs[0], closest_wall)[1]+1

    return (1/float(a_star_distance))**2


def f_monster_to_bomb(world, character = None):

    monsters = find_monsters(world)
    bombs = find_bombs(world)

    if len(bombs) == 0 or len(monsters) == 0:
        return 0

    closest_monster = closest_point(bombs[0], monsters, euclidean=False)

    a_star_distance = a_star(world, bombs[0], closest_monster)[1]+1

    return (1/float(a_star_distance))**2


# 1/(distance to closest wall)^2
def f_to_wall(world, character):
    character_location = (character.x, character.y)

    walls = find_walls(world)

    if len(walls) == 0:
        return 0

    closest_wall = closest_point(character_location, walls, euclidean=False)

    a_star_distance = a_star(world, character_location, closest_wall)[1]+1

    return (1 / float(a_star_distance)) ** 2


def number_walls(world, character = None):

    walls = find_walls(world)

    if len(walls) == 0:
        return 0

    #closest_wall = closest_point(character_location, walls, euclidean=False)

    # a_star_distance = a_star(world, character_location, closest_wall)[1]+1

    #I actually have no idea if this is a good implementation
    return (1 / float(len(walls))) ** 2

def number_monsters(world, character = None):

    monsters = find_monsters(world)

    if len(monsters) == 0:
        return 0

    #closest_wall = closest_point(character_location, walls, euclidean=False)

    # a_star_distance = a_star(world, character_location, closest_wall)[1]+1

    #I actually have no idea if this is a good implementation
    return (1 / float(len(monsters))) ** 2


# 1/(time to explosion of closest bomb)^2
def f_time_to_explosion(world, character):
    character_location = (character.x, character.y)

    bombs = find_bombs(world)

    if len(bombs) == 0:
        return 0

    (bx, by) = closest_point(character_location, bombs, euclidean=False)
    closest_bomb = world.bomb_at(bx, by)

    return (1 / float(closest_bomb.timer+1)) ** 2

# to see if the character is between a wall and map
# no 2 walls will ever form a corner so no implementation
def is_in_corner(world, character):
    world = SensedWorld.from_world(world)

    blocked_map_y = False
    blocked_map_x = False

    blocked_wall = False
    character_location = (character.x, character.y)

    if character_location[0] == 0:
        blocked_map_x = True

    if character_location[0] == world.width()-1:
        blocked_map_x = True

    if character_location[1] == 0:
        blocked_map_y = True

    if character_location[1] == world.height()-1:
        blocked_map_y = True

    if not blocked_map_x and not blocked_map_y:
        return 0

    if blocked_map_x and blocked_map_y:
        return 1

    if blocked_map_x and not blocked_map_y:
        if world.wall_at(character_location[0], character_location[1] + 1):
            blocked_wall = True
        if world.wall_at(character_location[0], character_location[1] - 1):
            blocked_wall = True

    if not blocked_map_x and blocked_map_y:
        if world.wall_at(character_location[0] + 1, character_location[1]):
            blocked_wall = True
        if world.wall_at(character_location[0] - 1, character_location[1]):
            blocked_wall = True

    if blocked_wall and (blocked_map_x or blocked_map_y):
        return 1

    return 0

def bomb_to_wall(world, character = None):
    world = SensedWorld.from_world(world)

    bomb = find_bombs(world)

    if len(bomb) == 0:
        return 0

    bomb = bomb[0]

    bomb_edge = False

    if bomb[0] == 0 or bomb[0] == world.width()-1:
        bomb_edge = True

    if bomb[1] == 0 or bomb[1] == world.height()-1:
        bomb_edge = True

    if bomb_edge:
        return 1

    return 0


# checks if character is inbetween bomb and monster
# by checking A* distances
# if char is closer to exit than monster, this is ignored
def between_monster_bomb(world, character):
    monsters = find_monsters(world)
    bombs = find_bombs(world)
    character_location = (character.x, character.y)

    if len(bombs) == 0 or len(monsters) == 0:
        return 0

    closest_monster = closest_point(bombs[0], monsters, euclidean=False)
    closest_bomb = closest_point(character_location, bombs, euclidean=False)

    a_star_distance_bomb_to_monster = a_star(world, closest_bomb, closest_monster)[1] + 1
    a_star_distance_char_to_monster = a_star(world, character_location, closest_monster)[1] + 1

    bomb = world.bomb_at(closest_bomb[0], closest_bomb[1])

    exits = find_exits(world)

    if len(exits) == 0:
        return 0

    closest_exit = closest_point(character_location, exits, euclidean=False)

    a_star_distance_char_to_exit = a_star(world, character_location, closest_exit)[1] + 1
    a_star_distance_monster_to_exit = a_star(world, closest_monster, closest_exit)[1] + 1


    if a_star_distance_char_to_monster < a_star_distance_bomb_to_monster:
        if a_star_distance_char_to_exit < a_star_distance_monster_to_exit:
            return 0
        return (1 / float(a_star_distance_char_to_monster)) ** 2

    return 0

# if chars distance to exit is lower than a monsters,
# the function returns 1
def race_to_exit(world, character):
    monsters = find_monsters(world)
    character_location = (character.x, character.y)
    exits = find_exits(world)
    if len(monsters) == 0 or len(exits) == 0:
        return 0

    closest_exit = closest_point(character_location, exits, euclidean=False)
    a_star_distance_char_to_exit = a_star(world, character_location, closest_exit)[1] + 1

    if len(monsters) == 1:
        closest_monster = closest_point(character_location, monsters, euclidean=False)
        a_star_distance_monster_to_exit = a_star(world, closest_monster, closest_exit)[1] + 1


        if a_star_distance_char_to_exit < a_star_distance_monster_to_exit:
            return 1
    else:
        a_star_distance_monster1_to_exit = a_star(world, monsters[0], closest_exit)[1] + 1
        a_star_distance_monster2_to_exit = a_star(world, monsters[1], closest_exit)[1] + 1

        if a_star_distance_monster1_to_exit < a_star_distance_monster2_to_exit:
            closest_monster = a_star_distance_monster1_to_exit
        else:
            closest_monster = a_star_distance_monster2_to_exit

        if a_star_distance_char_to_exit < closest_monster:
            return 1
    return 0

# checks to see if the character is in the bomb radius
# right as the bomb is [bomb radius] number of turns from exploding
def f_to_bomb_explosion(world, character):
    character_location = (character.x, character.y)
    bombs = find_bombs(world)

    if len(bombs) == 0:
        return 0.0

    closest_bomb = closest_point(character_location, bombs, euclidean=False)

    bomb = world.bomb_at(closest_bomb[0], closest_bomb[1])
    a_star_distance = a_star(world, character_location, closest_bomb)[1]+1


    if bomb.timer == world.expl_range and world.expl_range >= a_star_distance:
        return 1.0

    return 0.0

# checks to see if the bomb is near a wall
def f_wall_to_bomb(world, character = None):
    walls = find_walls(world)
    bombs = find_bombs(world)

    if len(bombs) == 0 or len(walls) == 0:
        return 0

    closest_wall = closest_point(bombs[0], walls, euclidean=False)

    a_star_distance = a_star(world, bombs[0], closest_wall)[1]+1

    return (1/float(a_star_distance))**2

# return 1 if the cell the character is in will explode, or has exploded
# return 0 if the cell the character is in will not explode
def f_is_exploded(world, character):
    if world.me(character) is None:
        return 1

    world = SensedWorld.from_world(world)

    character_location = (character.x, character.y)

    bombs = find_bombs(world)

    if len(bombs) == 0:
        return 0

    (bx, by) = closest_point(character_location, bombs, euclidean=False)
    closest_bomb = world.bomb_at(bx, by)

    world.add_blast(closest_bomb)

    if world.explosion_at(character.x, character.y) is not None:
        return 1
    else:
        return 0

def f_bomb_to_wall(world, character = None):
    bombs = find_bombs(world)
    walls = find_walls(world)

    if len(walls) == 0:
        return 1

    if len(bombs) == 0:
        return 0

    bomb = bombs[0]

    closest_wall = closest_point(bomb, walls)

    a_star_distance = a_star(world, bomb, closest_wall)[1] + 1

    return (1 / float(a_star_distance)) ** 2

def f_is_exploded_now(world, character):
    if world.me(character) is None:
        return 1
    
    if world.explosion_at(character.x, character.y) is not None:
        return 1
    
    world, _ = world.next()

    if world.explosion_at(character.x, character.y) is not None:
        return 1
        
    return 0