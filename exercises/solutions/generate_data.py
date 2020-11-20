import numpy as np

from matplotlib import pyplot as plt

# Numpy exercise
masses = np.loadtxt("exercises/numpy/masses.txt")
n_atoms = len(masses)

n_traj = 50
n_frames = 200
n_dims = 3

initial = np.asarray([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
], dtype=float)
initial += np.random.rand(n_atoms, n_dims)
t = np.linspace(1, 10, n_frames)
v0 = initial * np.random.rand(n_atoms, n_dims) / masses[:, None]
delta = np.multiply.outer(t, v0)
positions = 0.1 * np.max(delta) * np.random.rand(n_traj, n_frames, n_atoms, n_dims) + delta[None, :, :, :]

np.save("exercises/numpy/positions.npy", positions)


# Scipy exercise
n = 100
x = np.linspace(0, 2 * np.pi, num=n)

m = 0.43
h = 3.24

linear_data = m * x + h + 0.5 * np.random.randn(n)

A = 1.11
kappa = 0.37

exp_data = A * np.exp(kappa * (x + 0.3 * np.random.rand(n)))

np.savetxt("exercises/scipy/data.txt", np.asarray([x, linear_data, exp_data]).T)