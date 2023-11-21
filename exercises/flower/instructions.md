# Flower
## Goal

Find the color of a flower from its spectrum, as measured by Josina.

## Spectrum

Load the spectrum of the flower from the file `FlowerSpectrum.txt`, with `np.loadtxt`.

Have a look at the data file first, to understand what it means.

Then browse the documentation to find the correct optional argument to
1. Skip rows that do not contain data.
2. Use the non standard delimiter `;`.

Plot the spectrum, after removing the reference.

## Sensitivity

Do the same as for the spectrum, but with the file `Sensitivity.txt.`.

Beware that the file has a slightly different format than the previous.

Plot the sensitivity for each of the cones (identified by colors).

## Interpolate the spectrum

The spectrum and the sensitivity are given for different wavelengths. To be able to combine them, preventing to directly combine them.

To avoid that, use `numpy.interp` to interpolate the spectrum at the wavelength for which the sensitivity is known.

## Stimuli

Compute the stimuli $S_c$ for each cone with the formula

$$
S_c = \sum_f s_c(f) E(f),
$$

where $s_c(f)$ and $E(f)$ are respectively the sensitivitiy for the cone $c$ and the spectrum at frequency $f$.

## RGB

Define the vector of stimuli ${\rm\bf s} = (s_{red}, s_{green}, s_{blue})^T$ (mind the order!).

The RGB color is then $M {\rm\bf s}$, where $M$ is the conversion matrix stored in `cones_to_RGB.txt`.

Find a way to plot this color. It should be somwhate similar than in the picture of the flower.