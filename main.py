"""
Entrance of the program.
"""
from game import *
from postprocessing import *
import random


def main():
    random.seed(RANDOM_SEED)
    game = Game()
    while game.running and game.current_generation < N_GEN:
        game.reset()
        game.run()

    if PP_FORMULA or PP_GRAPH_VISUALIZATION:
        gs = [extract_computational_subgraph(ind) for ind in game.pop]

        for ind in game.pop:
            if ind.fitness is not None and ind.fitness > 350:
        # note that only the MU parents have been evaluated and have fitness values
                if PP_FORMULA:
                    print("Writing formula to ./pp/formula.txt ...")
                    with open("./pp/Trial{}/formulas.txt".format(TRIAL_NUMBER), 'w') as f:
                        for i, g in enumerate(gs):
                            formula = simplify(g, ['(rel_r)', '(cat_velocity_angle)', '(rel_r)'])
                            formula = round_expr(formula, PP_FORMULA_NUM_DIGITS)
                            print(
                                f"{i}\n score: {game.pop[i].fitness}\n formula: {formula}")
                            f.write(
                                f"{i}\n score: {game.pop[i].fitness}\n formula: {formula}\n")
                if PP_GRAPH_VISUALIZATION:
                    print("Drawing graphs to files in folder ./pp ...")
                    for i, g in enumerate(gs):
                        visualize(g, f"./pp/Trial{TRIAL_NUMBER}/{i}g{ind.fitness}.pdf", input_names=['rel_position', 'cat_velocity_angle', 'rel_position'])
                    flag = False
    print("DONE")

if __name__ == '__main__':
    main()