import numpy as np

def compute_dissipation_rate(a, grad_T_sq, Gamma0=0.1, kappa=1e-5, eta=2.7, alpha=0.5):
    """
    Eq.1: Γ = Γ₀ * (1 + κ|∇T±|²)^α * a^η
    """
    F_a = a ** eta
    grad_term = (1 + kappa * grad_T_sq) ** alpha
    return Gamma0 * grad_term * F_a
