"""
Inputs:
    Prob mutate 0-1
    max mutate size 0-2.5
    all/ single axis?
    weights 0-inf
    cooling type, speed

Outputs:
    Shape (average, min, max)
    Size (average, min, max)
    isosurface match {make image using paraview}
"""
import argparse
import os
import itertools
import numpy as np

#python .\ffeamesh\scripts\sim_anneal.py
#-m .\docs\molly_params\tutorial\thick_myosin\six_tets\myosin_thick.1
#-p 0.5
#-x 2.0
#-a
#-d low
#-w 1.0 1.0 1.0 1.0 1.0 1.0
#-v 0.01
#-f .\data\map_equilibrium_mystructrigor_15A_0p00202.mrc
#-o tmp/test_
#-c linear

def parse_probability(text):
    value = float(text)
    if value < 0.0 or value > 1.0:
        raise ValueError()

    return value

def parse_max(text):
    value = float(text)
    if value < 0.0:
        raise ValueError()

    return value

def get_args():
    """
    get the command line arguments
    Returns:
        (argparse.namespace)
    """
    parser = argparse.ArgumentParser()

    # parser.add_argument("-p",
    #                     "--mutate_prob",
    #                     type=parse_probability,
    #                     required=True,
    #                     help="mutate probability")

    # parser.add_argument("-x",
    #                     "--max_mutate",
    #                     type=parse_max,
    #                     default=1.0,
    #                     help="max mutate")

    parser.add_argument("-w",
                        "--weights",
                        type=float,
                        nargs='+',
                        help="enter weights")


    return parser.parse_args()

def main():
    args = get_args()
    path = ".\\docs\\molly_params\\tutorial\\thick_myosin\\six_tets\\myosin_thick.1"
    mrc_path = ".\\data\\map_equilibrium_mystructrigor_15A_0p00202.mrc"
    isovalue = 0.01
    cooling = "linear"

    probs = np.linspace(0.1, 0.9, 9)
    maxs = np.linspace(0.1, 5.0, 10)

    weights = ""
    for number in args.weights:
        weights+=f"{str(number)} "

    count = itertools.count(0)
    for prob in probs:
        for max in maxs:
            s = "python .\\ffeamesh\\scripts\\sim_anneal.py "
            s += f"-m {path} "
            s += f"-p {prob} "
            s += f"-x {max} "
            s += "-a "
            s += f"-d run_{next(count)}.csv "
            s += f"-w {weights} "
            s += f"-v {isovalue} "
            s += f"-f {mrc_path} "
            s += f"-c {cooling}"
            print(s)
            os.system(s)

if __name__ == "__main__":
    main()