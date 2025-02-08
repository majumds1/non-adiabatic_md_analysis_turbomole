#!/bin/bash

if [[ -f "path" ]]; then
	rm path
fi

# Read the molecule name from the file
mol_name=$(cat mol_name)

# Read the number of trajectories from the file
n_traj=$(cat n_traj)

# Read the number of excited states from the file
n_ex=$(cat n_excited_states)

# Read number of time steps of each trajectory
n_steps=2000   #Default
n_steps=$(cat n_steps)


# Loop through the trajectory directories
for ((i=1; i<=n_traj; i++)); do
    if [[ -d "${mol_name}_$i" ]]; then
        cd "${mol_name}_$i" || exit
        echo "Extracting data from trajectory $i"
##########################        
        for ((j=1; j<=n_ex; j++)); do
            grep "${j} a" exspectrum | awk '{print $4}' > "s${j}"
	    grep "${j} a" exspectrum | awk '{print $4}' > "osc${j}"
        done
##########################
        n_lines=0
        if [[ -f "s1" ]]; then 
		n_lines=$(wc -l < "s1")
        fi
##########################
        if ((n_lines>=n_steps)); then
	   echo "$(pwd)" >> ../path	
        fi   
##########################
        cd ..
    else
        echo "Trajectory $i does not exist"
    fi
done
