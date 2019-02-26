# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
from game import Game
from monsters.selfpreserving_monster import SelfPreservingMonster

sys.path.insert(1, '../group26')
from q_character import qCharacter
from q_learning import QLearner
from q_functions import *

from copy import deepcopy
import random
import time


def run(learner, seed):
    random.seed(seed)
    g = Game.fromfile('map.txt', display=False)
    g.add_monster(SelfPreservingMonster("monster",  # name
                                        "M",  # avatar
                                        3, 13,  # position
                                        2  # detection range
                                        ))

    g.add_character(qCharacter("me",  # name
                               "C",  # avatar
                               0, 0,  # position
                               learner,
                               False, 0, 0))

    # Run!
    g.go()
    return g.world.scores["me"]


functions = [f_to_exit, f_to_monster, f_to_bomb, f_is_exploded_now,
             f_bomb_exists, f_within_two_of_monster]

qLearner = QLearner(functions,
                    [8.467997328611984, -4.2234323520984125, -0.44748429577882354, -7.117769978109375,
                     7.499998201995708, -100])

ALPHA = .3

for i in range(0, 50):
    print("Running iteration #{}".format(i))
    seed = time.time()

    random.seed(time.time())
    weights = list(range(0, len(qLearner.weights)))
    random.shuffle(weights)
    for w in weights:
        print("\tRunning weight {}".format(w))

        j = 0
        while True:
            print("\t\tInner Iteration {}".format(j))

            random.seed(time.time())
            diff = random.random() * ALPHA
            print("\t\t\tDiff: {}".format(diff))

            qLearner_lower = QLearner(functions, deepcopy(qLearner.weights))
            qLearner_lower.weights[w] -= diff * qLearner_lower.weights[w]

            qLearner_higher = QLearner(functions, deepcopy(qLearner.weights))
            qLearner_higher.weights[w] += diff * qLearner_higher.weights[w]

            k = 0
            base_wins = 1
            while k < 100:
                if run(qLearner, seed+k) <= 0:
                    base_wins = 0
                    break
                k += 1

            print("\t\t\tBase: {}, {}".format(base_wins, qLearner.weights[w]))

            lower_wins = 0
            if run(qLearner_lower, seed + k) > 0:
                lower_wins += 1
            print("\t\t\tLower: {}, {}".format(lower_wins, qLearner_lower.weights[w]))

            higher_wins = 0
            if run(qLearner_higher, seed + k) > 0:
                higher_wins += 1
            print("\t\t\tHigher: {}, {}".format(higher_wins, qLearner_higher.weights[w]))

            if base_wins >= lower_wins and base_wins >= higher_wins:
                break
            elif lower_wins > higher_wins:
                qLearner.weights[w] = qLearner_lower.weights[w] * (lower_wins/5)
            else:
                qLearner.weights[w] = qLearner_higher.weights[w] * (higher_wins/5)
            j += 1

    print("\t{}".format(qLearner.weights))

print("Final Weights: {}".format(qLearner.weights))
