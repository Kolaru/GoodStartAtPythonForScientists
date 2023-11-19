# Numpy exercise

## Load data

Read masses from `masses.txt` using `np.loadtxt`.

Read the positions from `positions.npy` using `np.load`. The data has shape `(n_trajectory, n_snapshots, n_atoms, n_dims)`.

## Average trajectory

Compute the average trajectory.

Find the most average trajectory in the dataset. To do that find the trajectory that has the lowest distance to the average.

The distance between two trajectories $i$ and $j$ can be computed as

$$
\sum_{k = 1}^T \sum_{A = 1}^{n_A} \Vert {\rm\bf r}_{iA}(t_k) - {\rm\bf r}_{jA}(t_k) \Vert^2
$$

where ${\rm\bf r}_{iA}(t_k)$ is the position of atom $A$ in trajectory $i$ at the $k$th snapshot.

`np.argmin` gives you the index of the minimum element in an array and may prove useful.

## Center of mass

Compute the center of mass of each configuration and remove it from the coordinates to get centered data.

To check for consistency, write your code as a function that return the center of mass and check that the center of mass of your centered data is close to zero.
