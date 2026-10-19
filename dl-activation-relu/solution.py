import numpy as np


def relu_forward(x: np.ndarray) -> np.ndarray:
    ans=np.zeros(len(x))
    for i in range(len(x)):
        ans[i]=max(x[i],0)
    return ans


def relu_backward(grad_output: np.ndarray, x: np.ndarray) -> np.ndarray:
    ans = np.zeros(len(x))
    for i in range(len(x)):
        if x[i]>0:
            ans[i]=grad_output[i]
        else:
            ans[i]=0
    return ans
