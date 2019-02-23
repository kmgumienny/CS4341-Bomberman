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




#qLearner = QLearner([939568.8524203802, -2224.5011709235473, -1992.355258017747, 21483.29237836489, 7615.0355406307535, 1000])
qLearner = QLearner([988799.7073695898, -31368.22053567095, -22769.275594463747, 32488.45804630133, 48718.55666450353, -100])

for i in range(0, 0):
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
    print(qLearner.weights)
    print(g.world.scores["me"])

# Create the game
g = Game.fromfile('map.txt', display=True)

g.add_monster(StupidMonster("monster",  # name
                            "M",  # avatar
                            3, 9  # position
                            ))
g.add_character(qCharacter("me",  # name
                           "C",  # avatar
                           0, 0,  # position
                           qLearner,
                           False,
                           0,
                           1000))

# Run!
g.go()

print(qLearner.weights)