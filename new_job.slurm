#!/bin/bash

#SBATCH --job-name=new_job
#SBATCH --partition fake_comp
#SBATCH --nodes=616
#SBATCH --tasks-per-node=42
#SBATCH --time=09:00:00
#SBATCH -o new_job%.out
#SBATCH -e new_job%.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=nmp002@uark.edu

cd $SLURM_SUBMIT_DIR

# job command here: