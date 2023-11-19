# Correlation function from data

## Load data

Load the data `data.txt`, which represents an image of many blobs, and plot it with `pyplot.imshow`. The data is set in a 1 x 1 box.  Use `extent = (0, 1, 1, 0)` to have correct orientation of data.

## Thresholding

Use `skimage.filters.threshold_otsu` to get the bet threshold for the image. It means that by setting every value under the threshold to zero, and every value above the threshold to one, you get a binary imge that separate the blobs.

Plot the resulting binary image to verify each blob is indeed separated from the other.


## Labeling

Use `scipy.ndimage.label` to give a label to each blob. Then use the labels to get the average position of each blobs, using the grid of points you defined in step 2.

## Pair correlation

Consider the following code:

https://github.com/cfinch/Shocksolution_Examples/blob/master/PairCorrelation/paircorrelation.py

Use it to plot the pair correlation function of the blob and prove they are essentially uncorrelated.