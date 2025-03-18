import numpy as np

def energy_decay(t, E0=1e4, Gamma0=0.1, A=0.01, t0=1e17, sigma=1e16):
    """
    Eq.2-4: Global decay + localized mini-bangs.
    """
    # Global dissipation (Eq.2)
    E_tfm = E0 * np.exp(-Gamma0 * t)
    
    # Localized mini-bang (Eq.4)
    fluctuation = A * np.exp(-(t - t0)**2 / sigma**2)
    
    return E_tfm + fluctuation
