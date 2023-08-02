import numpy as np

from codes.utils.general import softmax


# return ahp weights
def ahp_weights(arr: np.ndarray):
    """modifiy by Taher"""

    soft_matrix = softmax(arr)
    return soft_matrix
