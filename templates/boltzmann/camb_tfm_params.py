def set_tfm_params(camb_params, Gamma0=0.1, eta=2.7):
    """
    Inject TFM dissipation terms into CAMB/CLASS parameters.
    """
    # Set dissipation rate Γ(a) = Γ0 * a^eta (Eq.1 simplified)
    camb_params.TFM_Gamma0 = Gamma0
    camb_params.TFM_eta = eta
    
    # Modify background equations (Eq.5)
    camb_params.WantCls = True
    camb_params.InitPower.set_params(ns=0.96, As=2e-9)
    
    # [ADAPT_THIS] - Add your modified Friedmann terms
    # ...
