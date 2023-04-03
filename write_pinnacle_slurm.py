#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script creates a .slurm file for jobs on the AHPCC cluster")

# add positional (required) arguments
parser.add_argument("job_name", help="The name of your job", type=str)

# add optional arguments
# the default for "store_true" is ... "False"
parser.add_argument('-q', '--queue', help='specifiy the queue to submit the job to (comp01, comp06, comp72) [default = comp01]',default = 'comp01',type=str)
parser.add_argument('-n', '--nodes', help='specifiy the number of nodes to run on [default = 1]',default = '1',type=str)
parser.add_argument('-p', '--processors', help='specify the number of processors to use [default = 1]',default = '1',type=str)
parser.add_argument('-t', '--walltime', help='specify the allotted number of hours for the job [default = 01]',default = '01',type=str)


# parse the actual arguments
# access argument values via "args" variable
args = parser.parse_args()


# create the slurm script

batch_script = open(args.job_name + '.slurm', 'w')
batch_script.write('#!/bin/bash\n\n\
#SBATCH --job-name=' + args.job_name + '\n\
#SBATCH --partition ')
batch_script.write(args.queue + '\n')


batch_script.write('#SBATCH --nodes=')

batch_script.write(args.nodes + '\n')

batch_script.write('#SBATCH --tasks-per-node=')

batch_script.write(args.processors + '\n')

batch_script.write('#SBATCH --time=')

batch_script.write(args.walltime + ':00:00\n')

batch_script.write('#SBATCH -o ' + args.job_name + '%.out\n\
#SBATCH -e ' + args.job_name + '%.err\n\
#SBATCH --mail-type=ALL\n\
#SBATCH --mail-user=nmp002@uark.edu\n\
\n\
cd $SLURM_SUBMIT_DIR\n\
\n\
# job command here:'
)

