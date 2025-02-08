#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
import numpy as np
import os


# Trajectories
file = open('path')
path = file.readlines()
n = len(path)                            # No. of trajectories


# No. of excited states
n_ex = int(np.loadtxt('n_excited_states'))
# No. of time steps
l = int(np.loadtxt('n_steps'))


# For storing data
Active = np.zeros([l, n])                                 # Active state
S = {i: np.zeros([l, n]) for i in range(1, n_ex+1)}       # Excitation energies
osc = {i: np.zeros([l, n]) for i in range(1, n_ex+1)}     # Oscillator strengths


# loop to read in active state from active file
A = []
for i in range(0,n):
    file = open(os.path.join(path[i].strip(),'active'))
    content = file.readlines()
    for j in range(2,10*l,2):
        A.append(int(content[j]))
        if(len(A) == l):
            break
    print(i)
    Active[:,i] = A
    A = []
    file.close()


# loop of read in excitation energies and oscillator sterngths
for i in range(0,n):
    for j in range(0,n_ex):
        file = np.loadtxt(os.path.join(path[i].strip(),f's{j+1}'))
        S[j+1][:,i]=file[0:l]
        file = np.loadtxt(os.path.join(path[i].strip(),f'osc{j+1}'))
        osc[j+1][:,i]=file[0:l]


# saving data to file
np.savetxt('active.dat', Active , delimiter=',')
for i in range(0,n_ex):
    np.savetxt(f's{i+1}.dat', S[i+1] , delimiter=',')
    np.savetxt(f'osc{i+1}.dat', osc[i+1] , delimiter=',')
