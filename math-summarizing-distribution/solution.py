import numpy as np
def skewness(x: np.ndarray) -> float:
    mean_val=np.mean(x)
    std_val=np.std(x)
    summation=0
    for i in range(len(x)):
        one_unit = (x[i]-mean_val)/std_val
        summation=summation + (one_unit)**3
    skewness=summation/len(x)
    return skewness


def summarize_distribution(x: np.ndarray) -> dict:
    return {"mean":np.mean(x),"median":np.median(x),"std":np.std(x),"skew":skewness(x)}
    pass
