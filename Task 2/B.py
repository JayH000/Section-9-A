import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 0.6  # Eccentricity
Tf = 200  # Final time
N = 400000  # Number of steps
dt = Tf / N  # Time step

# Initial conditions
q1, q2 = 1 - e, 0
p1, p2 = 0, np.sqrt((1 + e) / (1 - e))

# Arrays to store results
q1_symp, q2_symp = [q1], [q2]

# Symplectic Euler method
for _ in range(N):
    r = (q1**2 + q2**2)**1.5  # (q1^2 + q2^2)^(3/2)
    
    # Compute accelerations (Hamiltonian derivatives)
    dq1 = p1
    dq2 = p2
    dp1 = -q1 / r
    dp2 = -q2 / r

    # Update momenta first
    p1 += -dt * dp1
    p2 += -dt * dp2
    
    # Update positions
    q1 += dt * dq1
    q2 += dt * dq2

    # Store results
    q1_symp.append(q1)
    q2_symp.append(q2)




# Load explicit Euler data from the previous implementation
q1_explicit, q2_explicit = np.load("explicit_euler_orbit.npy")

# Plot both orbits
plt.figure(figsize=(8, 6))
plt.plot(q1_explicit, q2_explicit, label="Explicit Euler Orbit", color="blue", linestyle="dashed")
plt.plot(q1_symp, q2_symp, label="Symplectic Euler Orbit", color="green")
plt.scatter([0], [0], color="red", marker="o", label="Central Mass (Star)")
plt.xlabel("$q_1$")
plt.ylabel("$q_2$")
plt.title("Comparison of Explicit vs. Symplectic Euler Method")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
