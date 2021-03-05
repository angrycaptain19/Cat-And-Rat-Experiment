"""
Define some constant parameters and program settings.
"""

import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Cat And Rat AI via Evolutionary Cartesian Genetic Programming'
FPS = 60
IMG_DIR = './img'
SND_DIR = './snd'
FONT_NAME = 'Arial'
FONT_SIZE = 20
WHITE = (255, 255, 255)

RawInput = input("Trial Number|Acceleration|Max Velocity: ")

ProcessedInput = RawInput.split("|")

TRIAL_NUMBER = int(ProcessedInput[0])
if not os.path.exists('./pp/Trial{}'.format(TRIAL_NUMBER)):
    os.makedirs('./pp/Trial{}'.format(TRIAL_NUMBER))
CAT_ACCELERATION = float(ProcessedInput[1])
CAT_DAMPING = CAT_ACCELERATION/(float(ProcessedInput[2]))
with open("./pp/Trial{}/info.txt".format(TRIAL_NUMBER), "a") as file2:
    file2.write("Cat Acceleration = {} \n".format(CAT_ACCELERATION))
    file2.write("Cat Max Velocity = {} \n".format(CAT_ACCELERATION/CAT_DAMPING))
    file2.write("Acceleration Times Greater Than Rat = {} \n".format(CAT_ACCELERATION/1000))
    file2.write("Max Velocity Times Greater Than Rat = {}".format((CAT_ACCELERATION/CAT_DAMPING)/200))
# parameters of cartesian genetic programming
MUT_PB = 0.015  # mutate probability
N_COLS = 500   # number of cols (nodes) in a single-row CGP
LEVEL_BACK = 500  # how many levels back are allowed for inputs in CGP

# parameters of evolutionary strategy: MU+LAMBDA
MU = 1
LAMBDA = 9
N_GEN = 20  # max number of generations

# if True, then additional information will be printed
VERBOSE = True

PP_FORMULA = False
PP_FORMULA_NUM_DIGITS = 5
PP_FORMULA_SIMPLIFICATION = True
PP_GRAPH_VISUALIZATION = True

RANDOM_SEED = None
