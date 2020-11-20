from scipy.optimize import root_scalar


def f(x):
    return x**2 - 2


res = root_scalar(f, x0=1, x1=10)
print(res)