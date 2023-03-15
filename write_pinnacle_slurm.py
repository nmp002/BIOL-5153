#! /usr/bin/env python3

job_name = input('Enter a job name: ')
queue = input('Enter the queue you would like to use: ')
num_nodes = int(input('Enter the number of nodes: '))
num_cores = int(input('Enter the number of cores: '))
wall_time = input('Enter the time for the job, (formatted as hr:min:sec): ')
mail_type = input('Enter the desired mail type: ')
email = input('Enter your email: ')

print('#!/bin/bash')

print('#SBATCH --job-name=',job_name)
print('#SBATCH --partition ',queue)
print('#SBATCH --nodes=',num_nodes)
print('#SBATCH --tasks-per-node=',num_cores)
print('#SBATCH --time=',wall_time)
print('#SBATCH -o %',job_name,'.out')
print('#SBATCH -e %',job_name,'.err')
print('#SBATCH --mail-type=',mail_type)
print('#SBATCH --mail-user=',email)

print('cd $SLURM_SUMBIT_DIR')

print('# job command here')
