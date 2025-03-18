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
## How to Use These Files

1. **Einstein Toolkit Templates**:  
   - Copy `templates/einstein_toolkit/` to your Einstein Toolkit setup.  
   - Replace `[YOUR_TFM_TERMS_HERE]` with your implementation of Eqs.1-5.

2. **LISA Gravitational Waves**:  
   - Use `templates/hpc_jobs/run_lisa_echoes.slurm` as a SLURM template.  
   - Set `--Gamma0` and `--output` paths for your HPC cluster.

3. **CMB Analysis**:  
   - Modify `templates/boltzmann/camb_tfm_params.py` to inject TFM terms into CAMB/CLASS.  

## Validation Steps  
- **CMB**: Run CAMB/CLASS with your TFM-modified params and compare to Planck/WMAP data.  
- **LISA**: Simulate GW echoes using your HPC solver and analyze against LISA’s sensitivity curve.  
---

## Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/AliFayyazMalik/TFM-Cosmic-Fate.git
cd TFM-Cosmic-Fate

