import numpy as np


def sigmoid_forward(x: np.ndarray) -> np.ndarray:
    """Mirrors torch.sigmoid(x): 1 / (1 + exp(-x)). Clip x before exponentiating for numerical stability."""
    ans=np.zeros(len(x))
    for i in range(len(x)):
        ans[i]=1/(1+np.exp(-x[i]))
    return ans


def sigmoid_backward(grad_output: np.ndarray, output: np.ndarray) -> np.ndarray:
    ans=np.zeros(len(output))
    for i in range(len(output)):
        ans[i]=output[i]*(1-output[i])*grad_output[i]
    return ans
