from numpy import *

from matplotlib import pyplot as plt
from sklearn.neighbors import KernelDensity

N = 2500
maxiter = 10000
n_part = 1
i = 0

radius = sqrt(1 / (pi * N))
particles = [random.rand(2)]

while n_part < N and i < maxiter:
    i += 1
    pos = random.rand(2)
    d = asarray(particles) - pos[None, :]
    if all(linalg.norm(d, axis=1) > 2 * radius):
        n_part += 1
        particles.append(pos)

particles = asarray(particles)

kde = KernelDensity(kernel='gaussian', bandwidth=radius*0.5).fit(particles)

gridsize = 500
xx = linspace(0, 1, gridsize)
yy = xx

X, Y = meshgrid(xx, yy)
xy = vstack([Y.ravel(), X.ravel()]).T

density = exp(kde.score_samples(xy))
density = density.T.reshape(gridsize, gridsize)

print(density)

savetxt("exercises/final/data.txt", density)

plt.plot(particles[:, 0], particles[:, 1], "o")
plt.matshow(density, extent=(0, 1, 0, 1), cmap="gray")
plt.show()
