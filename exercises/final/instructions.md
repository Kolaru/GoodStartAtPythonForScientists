# Correlation function from data

## Load data

Load the data `data.txt` and plot it with `pyplot.imshow`. The data is set in a 1 x 1 box.  Use `extent = (0, 1, 1, 0)` to have correct orientation of data.

## Grid

Use `numpy.meshgrid` to create `x` and `y` components of each pixel in the image. Plot each points over the image with `pyplot.scatter` to make sure it is correctly aligned.

## Thresholding

Use `skimage.filters.threshold_otsu` to binarize the image. Plot the resulting binary image to verify each blob is indeed separated from the other.

## Labeling

Use `scipy.ndimage.label` to give a label to each blob. Then use the labels to get the average position of each blobs, using the grid of points you defined in step 2.

## Pair correlation

Consider the following code:

https://github.com/cfinch/Shocksolution_Examples/blob/master/PairCorrelation/paircorrelation.py

Use it to plot the pair correlation function of the blob and prove they are essentially uncorrelated.