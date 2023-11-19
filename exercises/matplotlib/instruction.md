# Matplotlib exercise

## Generate data

Generate two arrays of 10000 random normally distributed number with `np.random.randn`, representing `x` and `y` coordinate of random points respectively.

## Figure

Create a figure with 2 subplots (2 lines and 1 column) and shared y-axis (`sharey` option for `plt.subplots`).

## 1D subplot

On the first subplot, plot an histogram of the `x` coordinate with `ax.hist`, with the following properties:
    - Gray color
    - Normalized density
    - 30 bins

Over it plot the Gaussian distribution `1/sqrt(2*pi) * exp(-x**2 / 2)`. The two should very well coincide.

## 2D subplot

Get the value of the 2D histogram using `np.histrogram2D`. Be careful as the function returns 3 values, we are only interested in the first.

Plot the result with `ax.imshow`, with the following property:
    - Aspect ratio set to `"auto"` (keyword `"aspect"`)
    - Correct extent (keyword `"extent"`)

## Labels and legend

Set all the labels and add a legend to the first plot.