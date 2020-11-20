import numpy as np

from matplotlib import pyplot as plt
from scipy.optimize import curve_fit, root_scalar


def linear_fit(x, m, h):
    return m * x + h


data = np.loadtxt("exercises/scipy/data.txt")

x, linear, exponential = data.T

linear_params, linear_cov = curve_fit(linear_fit, x, linear)
log_params, log_cov = curve_fit(linear_fit, x, np.log(exponential))


def root_func(x):
    return linear_fit(x, *linear_params) - np.exp(linear_fit(x, *log_params))


res = root_scalar(root_func, x0=3.5, x1=4)


plt.plot(x, linear,
         linestyle="none",
         marker="o",
         label="Linear data")

plt.plot(x, exponential,
         linestyle="none",
         marker="s",
         label="Exponential data")

plt.plot(x, linear_fit(x, *linear_params),
         label="Linear fit")

plt.plot(x, np.exp(linear_fit(x, *log_params)),
         label="Exponential fit")

plt.annotate("Intersection",
             xy=[res.root, linear_fit(res.root, *linear_params)],
             xytext=[2, 8],
             arrowprops=dict(facecolor='black'))

plt.legend()
plt.show()
