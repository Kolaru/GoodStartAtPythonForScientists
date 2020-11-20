import numpy as np

from matplotlib import pyplot as plt

from matplotlib import rc

rc("text", usetex=True)

fig, axes = plt.subplots(2, 1, sharex=True)

normal_iidx = np.random.randn(10000)
normal_iidy = np.random.randn(10000)

gaussian_ax = axes[0]
gaussian_ax.hist(
    normal_iidx,
    bins=30,
    density=True,
    color="gray",
    label="Normalized count")

xx = np.linspace(-4, 4, 1000)
gaussian_ax.plot(
    xx,
    1 / np.sqrt(2 * np.pi) * np.exp(-xx**2 / 2),
    color="black",
    label="Analytical curve")
gaussian_ax.update({
    "ylabel": "Density"
})

gaussian_ax.legend()

H, xedges, yedges = np.histogram2d(
    normal_iidx,
    normal_iidy,
    bins=30)

density_ax = axes[1]
density_ax.imshow(
    H,
    aspect="auto",
    extent=(
        np.min(xedges),
        np.max(xedges),
        np.min(yedges),
        np.max(yedges)))

density_ax.update({
    "xlabel": "$x$ (a.u.)",
    "ylabel": "$y$ (a.u.)"
})
plt.show()
