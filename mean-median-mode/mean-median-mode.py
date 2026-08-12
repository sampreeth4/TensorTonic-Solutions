import numpy as np
from collections import Counter

def mean_median_mode(X):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    X = np.asarray(X)
    n = X.shape
    mean = float(np.mean(X))
    median= float(np.median(X))
    counts = Counter(X)
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    mode = float(min(modes))
    return mean, median, mode
