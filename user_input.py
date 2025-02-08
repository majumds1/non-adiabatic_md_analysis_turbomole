# Get user input
mol_name = input("Enter the molecule name (assuming trajectories are named molname_1, molename_2... : ")
n_traj = input("Enter the number of trajectories : ")
n_ex = input("Enter the number of excited states in your simulation : ")
n_steps = input("Enter the number of time steps in your simulation : ")

mol_name = mol_name.strip()
n_traj = n_traj.strip()
n_ex = n_ex.strip()
n_steps = n_steps.strip()

# Save to files
file = open("mol_name", "w") 
file.write(mol_name + "\n")
file.close()


file = open("n_traj", "w")
file.write(str(n_traj) + "\n")
file.close()


file = open("n_excited_states","w")
file.write(str(n_ex)+"\n")
file.close()


file = open("n_steps","w")
file.write(str(n_steps)+"\n")
file.close()

print(f"Saved molecule name: {mol_name} in file 'mol_name'")
print(f"Saved number of trajectories: {n_traj} in file 'n_traj'")
print(f"Saved number of excited states: {n_ex} in file 'n_excited_states'")
print(f"Saved number of time steps : {n_steps} in file 'n_steps'")
