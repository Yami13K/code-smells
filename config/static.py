from codes.utils.general import SessionState

SESSION_STATE = SessionState()

SMELLS = ["Abstraction", "Encapsulation", "Modularization", "Hierarchy"]

NAVIGATION = ["Git Repo", "Scores", "AHP picker", "Mapper",  "Profiling", "Clustering", ]

SUB_CATEGORIES = [
    "Modularity",
    "Analyzability",
    "Testability",
    "Modifiability",
    "Reusability",
]

METRICS_TO_SUB_CATEGORIES = {
    "WMC": SUB_CATEGORIES[:3],
    "DIT": [SUB_CATEGORIES[3]],
    "NOC": [SUB_CATEGORIES[3]],
    "CBO": SUB_CATEGORIES[2::2],
    "RFC": SUB_CATEGORIES[1::3],
    "LCOM": [SUB_CATEGORIES[-1]],
}

METRICS = [
    "WMC",
    "DIT",
    "NOC",
    "CBO",
    "RFC",
    "LCOM",
]

SMELLS_TO_METRICS = {
    "Abstraction": [*METRICS[:2], METRICS[-1]],
    "Encapsulation": [METRICS[3]],
    "Modularization": [METRICS[0], METRICS[3], METRICS[-1]],
    "Hierarchy": METRICS[1:3],
}

WARNING = 'please input a github repo first in the first section'
