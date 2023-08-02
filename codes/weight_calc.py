import numpy as np
import pandas as pd

from codes.stub import AHP_SCORES
from codes.utils.df import calculate_score
from codes.utils.general import softmax
from config.static import *


def calculate_metric_sum(metric_to_qualities, quality_to_value):
    return {
        metric: sum(quality_to_value[quality] for quality in qualities)
        for metric, qualities in metric_to_qualities.items()
    }


def normalize_dicts(original_dict: dict):
    values = np.array(list(original_dict.values()))
    softmax_output = softmax(values)
    softmax_dict = {
        key: value for key, value in zip(original_dict.keys(), softmax_output)
    }
    return softmax_dict


def score_pipeline(df: pd.DataFrame):
    quality_to_value = dict(zip(SUB_CATEGORIES, AHP_SCORES))
    metric_sums = calculate_metric_sum(METRICS_TO_SUB_CATEGORIES, quality_to_value)
    soft_metrics = normalize_dicts(metric_sums)

    smells_weights_dict = normalize_dicts(
        calculate_metric_sum(SMELLS_TO_METRICS, soft_metrics)
    )

    weights = smells_weights_dict.values()

    scores_df = calculate_score(df, weights)
    return scores_df
