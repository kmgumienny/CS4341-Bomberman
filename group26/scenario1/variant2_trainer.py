# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.stupid_monster import StupidMonster

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner




qLearner = QLearner([1, -1, -1, 1, -1, -1])


for i in range(0, 100):
    print("Running iteration #"+str(i))
    # Create the game
    g = Game.fromfile('map.txt', display=False)

    g.add_monster(StupidMonster("monster",  # name
                                "M",  # avatar
                                3, 9  # position
                                ))

    g.add_character(qCharacter("me", # name
                                  "C",  # avatar
                                  0, 0,  # position
                               qLearner,
                               True,
                               i,
                               1000))
    # Run!
    g.go()
    print(g.world.scores["me"])

# # Create the game
# g = Game.fromfile('map.txt', display=True)
#
# g.add_character(qCharacter("me",  # name
#                            "C",  # avatar
#                            0, 0,  # position
#                            qLearner,
#                            False,
#                            i,
#                            1000))
#
# # Run!
# g.go()

print(qLearner.weights)