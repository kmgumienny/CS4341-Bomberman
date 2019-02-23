import math
import sys
sys.path.insert(0, '../bomberman')

from world_utilities import *


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


# 1/(distance to closest wall)^2
def f_to_wall(world, character):
    character_location = (character.x, character.y)

    walls = find_walls(world)

    if len(walls) == 0:
        return 0

    closest_wall = closest_point(character_location, walls, euclidean=False)

    a_star_distance = a_star(world, character_location, closest_wall)[1]+1

    return (1 / float(a_star_distance)) ** 2


# 1/(time to explosion of closest bomb)^2
def f_time_to_explosion(world, character):
    character_location = (character.x, character.y)

    bombs = find_bombs(world)

    if len(bombs) == 0:
        return 0

    (bx, by) = closest_point(character_location, bombs, euclidean=False)
    closest_bomb = world.bomb_at(bx, by)

    return (1 / float(closest_bomb.timer+1)) ** 2


# return 1 if the cell the character is in will explode, or has exploded
# return 0 if the cell the character is in will not explode
def f_is_exploded(world, character):
    if world.me(character) is None:
        return 1

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