import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import argparse

# Load data
Active = np.loadtxt('active.dat', delimiter=',',unpack=True) 
n = len(Active[:,0])


# No. of time steps
l = int(np.loadtxt('n_steps'))


# No. of excited states
n_ex = int(np.loadtxt('n_excited_states'))


# Time step size
step_size = float(np.loadtxt('step_size'))


# Set up the argument parser
parser = argparse.ArgumentParser(description="Plot population analysis from NAMD trajectory data")
parser.add_argument('-s', '--start', type=int, required=True, help="start time step")
parser.add_argument('-e', '--end', type=int, required=True, help="end timestep")

# Parse arguments
args = parser.parse_args()
start = args.start
end = args.end

if start < 0 or end > l or start >= end:
    print("Invalid bounds for start and end timesteps. Please provide valid values.")
    exit()


# Calculate population of states
P = {i: np.zeros(l) for i in range(0,n_ex+1)} 
for i in range(0,n):
    for j in range(0,l):
        for state in range(0,n_ex+1):
            if (Active[i,j] == state):
                P[state][j] = P[state][j] + 1

for state in range(0,n_ex+1):
    for i in range(0,l):
          P[state][i] = P[state][i]/float(n)


# Time step tracker
t=np.zeros(l)
for i in range(1,l):
    t[i] = t[i-1] + step_size


# Plot
colors = ['blue', 'green', 'red', 'purple', 'brown', 'orange','pink', 'gray', 'olive', 'cyan']
for i in range(0,n_ex+1):
    plt.plot(t[start:end],P[i][start:end],label=f'S{i}', color=colors[i%len(colors)])

plt.title('Population Aanalysis')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.savefig('population.png', dpi=400, bbox_inches='tight')
