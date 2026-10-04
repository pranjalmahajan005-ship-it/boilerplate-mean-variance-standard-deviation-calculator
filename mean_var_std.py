import numpy as np

def calculate(list): if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(lst).reshape(3, 3)

    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    return {
        name: [f(a, axis=0).tolist(), f(a, axis=1).tolist(), f(a).item()]
        for name, f in funcs.items()
    }
