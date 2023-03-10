---
# **BIOL 5153: Assignment 3**
### Nicholas Powell
### March 10th, 2023
---
## **Description:**

- Compares an unknown sequence to a blast database of genomes remotely
- Synchronizes the remote genomes to my local genomes set

---

**1. Use rsync to upload the mt_genomes directory onto the AHPCC in /storage/username:**
```
rsync -av mt_genomes nmp002@hpc-portal2.hpc.uark.edu/storage/nmp002
```

**2. Use scp or rsync to upload ‘unknown.fa’, which contains an unknown sequence:** 
```
scp unknown.fa nmp002@hpc-portal2.hpc.uark.edu:/storage/nmp002/mt_genomes
```

**3. Write a slurm script for the job:** 
```
nano assn3.slurm
```

Inside nano:
```
#!/bin/bash

#SBATCH --job-name=unknown_sequence
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=1
#SBATCH --time=00:01:00
#SBATCH -o assn3_%j.out
#SBATCH -e assn3_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=nmp002@uark.edu

# export OMP_NUM_THREADS=32

module purge
module load blast
cat /storage/nmp002/mt_genomes/*.fasta > /storage/nmp002/mt_genomes/genomes.fas
makeblastdb -in genomes.fas -dbtype nucl
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn

cd $SLURM_SUBMIT_DIR
```

Copy the .slurm file to the cluster:

```
scp assn3.slurm  nmp002@hpc-portal2.hpc.uark.edu:/storage/nmp002/mt_genomes
```

On AHPCC cluster:

```
cd /storage/nmp002/mt_genomes
nano assn3.slurm	# to check that the script contains everything I want to run
sbatch assn3.slurm	# upload the job 
stat | grep nmp002	# to see where I am in the queue
```

**4. Use rsync to synchronize the remote mt_genomes and your local version of mt_genomes:**
```
rsync -av nmp002@hpc-portal2.hpc.uark.edu:/storage/nmp002/mt_genomes/ .
```

**5. Answers:**
  
   **Time for job to complete:** 3 seconds  
   **Closest match in the database:** Cucurbita


