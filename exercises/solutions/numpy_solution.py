import numpy as np

# Load data

masses = np.loadtxt("exercises/numpy/masses.txt")
positions = np.load("exercises/numpy/positions.npy")


# Average trajectory

avg_traj = np.mean(positions, axis=0)
diff = np.sum((positions - avg_traj[None, :, :, :])**2, axis=(1, 2, 3))
ind = np.argmin(diff, axis=0)

print(f"Most average trajectory is {ind}")


# Center of mass

def center_of_mass(positions, masses):
    weighted_pos = positions * masses[None, None, :, None]
    return np.sum(weighted_pos, axis=2) / np.sum(masses)

cm = center_of_mass(positions, masses)
centered_pos = positions - cm[:, :, None, :]
