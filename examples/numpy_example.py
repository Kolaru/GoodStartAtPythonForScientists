import numpy as np

# Example 1: Elementwise and reduction
# Integrate a the function sin(x) + x between 0 and pi
# Result should be close to pi**2/2 + 2 = 6.9348

xx = np.linspace(0, np.pi, 1000)
yy = np.sin(xx) + xx

areas = (yy[:-1] + yy[1:]) / 2 * (xx[1:] - xx[:-1])

res = np.sum(areas)

# Example 2: Advanced indexing
# Ising model
# L x N x N box
# Populate with magnetization mk for spins in layer k
# Compute average spin per layer
# Compute total energy E(s1 s2) = -J s1 s2

N = 20
L = 10
mm = np.linspace(0, 1, L)
up_proba = 0.5 * (mm + 1)

spins = -np.ones((L, N, N), dtype=int)
r = np.random.rand(L, N, N)

ups = r < up_proba[:, None, None]
spins[ups] = 1

magnetizations = np.mean(spins, axis=(1, 2))

J = 1

next_directions = np.asarray([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

energies = np.zeros((L, N, N))

Jx = 1
Jy = 1.2
Jz = 0.5

energies[:-1, :, :] += Jx * spins[:-1, :, :] * spins[1:, :, :]
energies[:, :-1, :] += Jy * spins[:, :-1, :] * spins[:, 1:, :]
energies[:, :, :-1] += Jz * spins[:, :, :-1] * spins[:, :, 1:]

Etot = np.sum(energies)
