#!/bin/bash
#SBATCH --job-name=TFM_LISA_GW
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=128
#SBATCH --time=24:00:00

# Load modules
module load einsteintoolkit
module load python/3.9

# Run GW echo simulation (ADAPT PATHS!)
srun -n 512 ./path/to/your_gw_solver \
  --Gamma0 $(python -c "from src.params.constants import Gamma0; print(Gamma0)") \
  --output lisa_gw_echoes.h5

# Postprocess (customize)
python your_postprocessing_script.py lisa_gw_echoes.h5
