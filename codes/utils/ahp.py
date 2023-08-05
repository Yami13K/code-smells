import numpy as np

from codes.utils.general import softmax
import json


# return ahp weights
def ahp_weights(arr: np.ndarray):
    """modifiy by Taher"""

    soft_matrix = softmax(arr)
    return soft_matrix


def save_matrix_json(matrix, filename):

    with open(filename, "w") as json_file:
        json.dump(matrix, json_file, indent=4)


def load_json_matrix(filename):
    with open(filename, "r") as json_file:
        matrix = json.load(json_file)

    return matrix
