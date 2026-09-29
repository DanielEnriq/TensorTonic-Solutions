from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    
    mode = x[0]
    counts = dict()
    
    for num in x:
        if num not in counts.keys():
            counts[num] = 0
        counts[num] += 1

    high = max(counts.values())
    mode = min([candidate for candidate in counts.keys() if counts[candidate] == high])
    return {"mean" : float(np.mean(x)), "median" : float(np.median(x)), "mode" : float(mode)}

    