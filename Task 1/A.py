import numpy as np
import scipy.integrate as spi

# Constants
k = 1.38064852e-23  # Boltzmann constant (J/K)
h = 6.626e-34       # Planck constant (J·s)
c = 3.0e8           # Speed of light (m/s)
pi = np.pi
hbar = h / (2 * pi)

# Prefactor
prefactor = (k**4) / (4 * (c**2) * (hbar**3) * (pi**2))

# True value for verification
true_value = 5.670367e-8  # W/m²K⁴

# Function to integrate
def integrand(z):
    x = z / (1 - z)
    return (z**3 / (1 - z)**5) / (np.exp(x) - 1)

# Perform numerical integration
result, error = spi.quad(integrand, 0, 1)

# Multiply by prefactor
W = 2 * pi * prefactor * result

# Print results
print(f"Numerical Result: {W:.10e} W/m²K⁴")
print(f"True Value: {true_value:.10e} W/m²K⁴")
print(f"Absolute Error: {abs(W - true_value):.10e}")
print(f"Relative Error: {abs(W - true_value) / true_value:.10%}")
