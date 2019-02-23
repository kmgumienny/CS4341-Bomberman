

def getState(world, character, size):
    state = []
    for x in range(character.x -  size, character.x + size + 1):
        if x >= 0 and x < world.width():
            xstate = []
            
            for y in range(character.y -  size, character.y + size + 1):
                if y >= 0 and y < world.height():
                    if world.empty_at(x, y):
                        xstate += [' ']
                    elif world.wall_at(x, y):
                        xstate += ['W']
                    elif world.bomb_at(x, y):
                        xstate += ['B']
                    elif world.explosion_at(x, y):
                        xstate += ['X']
                    elif world.monsters_at(x, y) != None:
                        xstate += ['M']
                    elif world.characters_at(x, y) != None:
                        xstate += ['C']
                    elif world.exit_at(x, y):
                        xstate += ['E']
                else:
                    state += [xstate]
        else:
            state += [[]]
            
    return str(state)