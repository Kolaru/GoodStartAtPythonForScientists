import numpy as np

from matplotlib import pyplot as plt
from scipy import ndimage
from skimage.filters import threshold_otsu

# https://github.com/cfinch/Shocksolution_Examples/blob/master/PairCorrelation/paircorrelation.py
def pairCorrelationFunction_2D(x, y, S, rMax, dr):
    """Compute the two-dimensional pair correlation function, also known
    as the radial distribution function, for a set of circular particles
    contained in a square region of a plane.  This simple function finds
    reference particles such that a circle of radius rMax drawn around the
    particle will fit entirely within the square, eliminating the need to
    compensate for edge effects.  If no such particles exist, an error is
    returned. Try a smaller rMax...or write some code to handle edge effects! ;)
    Arguments:
        x               an array of x positions of centers of particles
        y               an array of y positions of centers of particles
        S               length of each side of the square region of the plane
        rMax            outer diameter of largest annulus
        dr              increment for increasing radius of annulus
    Returns a tuple: (g, radii, interior_indices)
        g(r)            a numpy array containing the correlation function g(r)
        radii           a numpy array containing the radii of the
                        annuli used to compute g(r)
        reference_indices   indices of reference particles
    """
    from numpy import zeros, sqrt, where, pi, mean, arange, histogram
    # Number of particles in ring/area of ring/number of reference particles/number density
    # area of ring = pi*(r_outer**2 - r_inner**2)

    # Find particles which are close enough to the box center that a circle of radius
    # rMax will not cross any edge of the box
    bools1 = x > rMax
    bools2 = x < (S - rMax)
    bools3 = y > rMax
    bools4 = y < (S - rMax)
    interior_indices, = where(bools1 * bools2 * bools3 * bools4)
    num_interior_particles = len(interior_indices)

    if num_interior_particles < 1:
        raise  RuntimeError ("No particles found for which a circle of radius rMax\
                will lie entirely within a square of side length S.  Decrease rMax\
                or increase the size of the square.")

    edges = arange(0., rMax + 1.1 * dr, dr)
    num_increments = len(edges) - 1
    g = zeros([num_interior_particles, num_increments])
    radii = zeros(num_increments)
    numberDensity = len(x) / S**2

    # Compute pairwise correlation for each interior particle
    for p in range(num_interior_particles):
        index = interior_indices[p]
        d = sqrt((x[index] - x)**2 + (y[index] - y)**2)
        d[index] = 2 * rMax

        (result, bins) = histogram(d, bins=edges, normed=False)
        g[p, :] = result/numberDensity

    # Average g(r) for all interior particles and compute radii
    g_average = zeros(num_increments)
    for i in range(num_increments):
        radii[i] = (edges[i] + edges[i+1]) / 2.
        rOuter = edges[i + 1]
        rInner = edges[i]
        g_average[i] = mean(g[:, i]) / (pi * (rOuter**2 - rInner**2))

    return (g_average, radii, interior_indices)


data = np.loadtxt("exercises/final/data.txt")
extent = (0, 1, 1, 0)
shape = data.shape

XX, YY = np.meshgrid(
    (np.arange(shape[0]) + 0.5) / shape[0],
    (np.arange(shape[1]) + 0.5) / shape[1])

thres = threshold_otsu(data)
binary = data > thres

labels, num_blobs = ndimage.label(binary)
num_blobs -= 1  # Remove background
labels -= 1

blob_x = np.zeros(num_blobs)
blob_y = np.zeros(num_blobs)

for i in range(num_blobs):
    blob_x[i] = np.mean(XX[labels == i])
    blob_y[i] = np.mean(YY[labels == i])

g, radii, interior_indices = pairCorrelationFunction_2D(blob_x, blob_y, 1, 0.4, 0.005)
plt.plot(radii, g)
plt.figure()
plt.imshow(data, cmap="gray", extent=extent)

plt.imshow(binary, cmap="gray", extent=extent)
plt.scatter(blob_x, blob_y, color="red", marker=".")
plt.show()
