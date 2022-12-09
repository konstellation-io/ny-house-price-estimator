"""
Reusable visualization code
"""

from typing import Union

import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(
        y_pred: np.ndarray,
        y_true: np.ndarray,
        filepath: str,
        classes: Union[list, tuple] = (0, 1, 2, 3),
        labels: Union[list, tuple] = ("low", "mid", "high", "lux"),
) -> None:
    """
    Given arrays for predictions (y_pred) and true values (y_true) of a binary variable, plots a confusion matrix for
    the classes with their provided labels and saves it to the location specified in filepath.
    """
    conf_matrix = confusion_matrix(y_true, y_pred)
    conf_matrix = conf_matrix / conf_matrix.sum(axis=1).reshape(
        len(classes), 1)

    _ = plt.subplots(figsize=(10, 10))
    sns.heatmap(
        conf_matrix,
        annot=True,
        cmap="BuGn",
        square=True,
        fmt=".2f",
        annot_kws={"size": 10},
        cbar=False,
    )
    plt.xlabel("Predicted", fontsize=16)
    plt.ylabel("Real", fontsize=16)
    plt.xticks(ticks=np.arange(0.5, len(classes)),
               labels=labels,
               rotation=0,
               fontsize=12)
    plt.yticks(ticks=np.arange(0.5, len(classes)),
               labels=labels,
               rotation=0,
               fontsize=12)

    plt.savefig(filepath)
    plt.close()
