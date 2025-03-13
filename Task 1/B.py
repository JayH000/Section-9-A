import numpy as np
from scipy.integrate import fixed_quad

# Constants
k = 1.38064852e-23  # Boltzmann constant (J/K)
h = 6.626e-34       # Planck's constant (J·s)
c = 3.0e8           # Speed of light (m/s)
pi = np.pi          # Pi

# Prefactor for Stefan-Boltzmann constant
prefactor = (2 * pi**5 * k**4) / (15 * c**2 * h**3)

# Function for transformed integral
def integrand(z):
    x = z / (1 - z)
    return (x**3 / (np.exp(x) - 1)) * (1 / (1 - z)**2)

# Use fixed_quad for numerical integration
sigma_integral, _ = fixed_quad(integrand, 0, 1, n=10)  # n is the number of points

# Compute Stefan-Boltzmann constant
sigma_numeric = prefactor * sigma_integral

# True value for comparison
sigma_true = 5.670367e-8  # W/m²K⁴

# Print results
print(f"Computed σ using fixed_quad: {sigma_numeric:.10e} W/m²K⁴")
print(f"True σ: {sigma_true:.10e} W/m²K⁴")
print(f"Relative Error: {abs(sigma_numeric - sigma_true) / sigma_true:.2e}")
