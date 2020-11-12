# Numpy exercise

## Generate data

Generate two array of 10000 random uniform number with `np.random.randn`, representing `x` and `y` coordinate of random points respectively.

## Figure

Create a figure with 3 subplots (3 lines and 1 column) and shared y-axis.

## 1D subplot

On the first subplot, plot an histogram of the `x` coordinate with `ax.hist`, with the following properties:
    - Gray color
    - Normalized density
    - 30 bins

Over it plot the Gaussian distribution `1/sqrt(2*pi) * exp(-x**2 / 2)`. The two should very well coincide.

## 2D subplot

Get the value of the 2D histogram using `np.histrogram2D`. Be careful as the function returns 3 values, we hare mainly interested in the first.

Plot the result with `ax.imshow`, with the following property:
    - Aspect ratio set to `"auto"` (keyword `"aspect"`)
    - Correct extent (keyword `"extent"`)

## Labels and legend

Set all the labels and a legend in the first plot.