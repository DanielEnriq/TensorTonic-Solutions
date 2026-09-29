import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y_h = np.asarray(y_pred)
    y = np.asarray(y_true)

    return np.mean(np.square(y_h -y))