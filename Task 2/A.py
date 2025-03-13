import numpy as np
import matplotlib.pyplot as plt

# Constants
e = 0.6  # Eccentricity
Tf = 200  # Final time
N = 100000  # Number of steps
dt = Tf / N  # Time step

# Initial conditions
q1, q2 = 1 - e, 0
p1, p2 = 0, np.sqrt((1 + e) / (1 - e))

# Arrays to store results
q1_values, q2_values = [q1], [q2]

# Explicit Euler method
for _ in range(N):
    r = (q1**2 + q2**2)**1.5  # (q1^2 + q2^2)^(3/2)
    
    # Compute accelerations (dp/dt)
    dp1 = -q1 / r
    dp2 = -q2 / r
    
    # Update momenta
    p1 += dt * dp1
    p2 += dt * dp2
    
    # Update positions
    q1 += dt * p1
    q2 += dt * p2

    # Store results
    q1_values.append(q1)
    q2_values.append(q2)

# Plot the orbit
plt.figure(figsize=(8, 6))
plt.plot(q1_values, q2_values, label="Planet Orbit", color="blue")
plt.scatter([0], [0], color="red", marker="o", label="Central Mass (Star)")
plt.xlabel("$q_1$")
plt.ylabel("$q_2$")
plt.title("Planet Orbit using Explicit Euler Method")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
