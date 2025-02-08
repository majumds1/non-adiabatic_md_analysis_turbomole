# non-adiabatic_md_analysis_turbomole
Repository of scripts for data extraction, analysis and computation of steady state and time resolved spectroscopic observables from non-adiabatic molecular dynamics trajectories in TURBOMOLE.

Usage,
1. Run python script "user_input.py" and provide simulation details such as molecule name, number of trajectories, number of time steps, etc.

2. Run bash script "setup_namd.sh" to extract data from the trajectory directories

3. Run python script data_namd.py to compile data from all trajectories for further analysis

4. Run python script "population.py" with start and end time steps to generate population analysis plot. Feel free to modify the scripts as required.


Example usage,

In the directory containing the trajectories run the following commands,

python user_input.py

bash setup_namd.sh

python data_namd.py

python population.py -s 0 -e 3000

Output - population.png


Setting up python environment - if the python environment is not set up already, it can be set up by following these simple steps,

a. Install Conda/Miniconda
   Download anaconda/miniconda installer (or use curl)
   bash Miniconda.sh

b. Create and activate conda environment,
   conda create -n namd_analysis
   conda activate namd_analysis

c. Install required packages,
   conda install numpy
   conda install matplotlib

d. Procedd with the steps above for NAMD analysis.


Relevant paper for citation, 

Majumdar, Sourav, et al. "Mechanism of the Non‐Kasha Fluorescence in Pyrene." Journal of Computational Chemistry 46.3 (2025): e70040. doi:https://doi.org/10.1002/jcc.70040  
