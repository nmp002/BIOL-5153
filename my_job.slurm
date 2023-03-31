#!/bin/bash

#SBATCH --job-name=my_job
#SBATCH --partition comp01
#SBATCH --nodes=32
#SBATCH --tasks-per-node=1
#SBATCH --time=01:00:00
#SBATCH -o my_job%.out
#SBATCH -e my_job%.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=nmp002@uark.edu

cd $SLURM_SUBMIT_DIR

# job command here