# TFM-Cosmic-Fate  
**Code templates for simulating cosmic dissipation, stabilization, and gravitational wave echoes in the Time Field Model (TFM)**  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
**⚠️ Disclaimer**: This repository contains *theoretical frameworks and synthetic data only*. No real HPC simulations or observational datasets are included.  

---

## Purpose  
This repository provides:  
- **Templates** to run TFM cosmic fate simulations on HPC clusters (Einstein Toolkit/CAMB/CLASS).  
- **Theoretical models** for dissipation rate (Γ), modified Friedmann equations, and gravitational wave echoes.  
- **Validation guidelines** to compare TFM predictions against Planck/WMAP/LISA data.  

**You must supply your own observational/HPC data** to test TFM.  

---

## Key Features  
1. **Modified Einstein Toolkit Configurations**  
   - `templates/einstein_toolkit/`: TFM-compatible parameter files for curvature evolution (`McLachlan`) and hydrodynamics (`GRHydro`).  
2. **CMB Power Spectrum Integration**  
   - `templates/boltzmann/camb_tfm_params.py`: Adds TFM dissipation terms to CAMB/CLASS.  
3. **LISA Gravitational Wave Templates**  
   - `src/params/lisa_config.yml`: Frequency bands and strain thresholds for Eq.8.  

---

## Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/AliFayyazMalik/TFM-Cosmic-Fate.git
cd TFM-Cosmic-Fate
