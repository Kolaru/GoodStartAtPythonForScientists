import numpy as np
from matplotlib import pyplot as plt
# from skimage.filters import threshold_otsu as otsu
from scipy.ndimage import label

data = np.loadtxt("exercises/final/data.txt")
centers = np.linspace(0.5/500, 1 - 0.5/500, 500)

X, Y = np.meshgrid(centers, centers)

thres = 1.6
binary = data > 1.6
binary = np.zeros_like(data)
binary[data > 1.6] = 1

labels, n = label(binary)

avg_x = []
avg_y = []

for i in range(n):
    xblob = X[labels == i]
    yblob = Y[labels == i]

    avg_x.append(np.mean(xblob))
    avg_y.append(np.mean(yblob))


fig, axes = plt.subplots(2, 2)

axes[0, 0].imshow(data, extent = (0, 1, 1, 0))

axes[0, 1].imshow(data, extent = (0, 1, 1, 0))
# axes[0, 1].scatter(X, Y, color = "red")
axes[0, 1].update({
    "xlim": (0.2, 0.25),
    "ylim": (0.8, 0.85)
})

axes[1, 0].imshow(labels, extent = (0, 1, 1, 0))
axes[1, 0].update({
    "xlim": (0.2, 0.25),
    "ylim": (0.8, 0.85)
})

axes[1, 1].imshow(binary, extent = (0, 1, 1, 0))
# axes[0, 1].scatter(X, Y, color = "red")
axes[1, 1].update({
    "xlim": (0.2, 0.25),
    "ylim": (0.8, 0.85)
})

axes[1, 1].scatter(avg_x, avg_y, color = "red")

plt.show()