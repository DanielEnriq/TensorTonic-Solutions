import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a_vec = np.asarray(a, dtype=np.float32)
    b_vec = np.asarray(b, dtype=np.float32)

    norm_a = np.sqrt(np.sum(np.square(a_vec)))
    norm_b = np.sqrt(np.sum(np.square(b_vec)))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    else:
        return float(np.dot(a_vec, b_vec) / (norm_a * norm_b))