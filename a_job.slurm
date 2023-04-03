#!/bin/bash

#SBATCH --job-name=a_job
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --tasks-per-node=30
#SBATCH --time=01:00:00
#SBATCH -o a_job%.out
#SBATCH -e a_job%.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=nmp002@uark.edu

cd $SLURM_SUBMIT_DIR

# job command here: