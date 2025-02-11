import numpy as np
import matplotlib.pyplot as plt
import math
import argparse


# User arguments
parser = argparse.ArgumentParser(description="Compute and plot fluorescence spectrum.")
parser.add_argument('-l', "--lineshape", choices=['g', 'l'], default='l',help="Lineshape function:'g' for Gaussian,'l' for Lorentzian,")
parser.add_argument('-w', "--linewidth", type=float,default=0.05, help="linewidth en eV")
parser.add_argument('-s', "--shift", type=float,default=0.0, help="red (-ve) or blue (+ve) shift in eV")
args = parser.parse_args()


# Load options
sigma = args.linewidth   # in eV
ls = args.lineshape
shift=args.shift


# prefactor
pf = 2*np.pi*137.036**3


# shift  
def apply_shift(A, shift):
    l = len(A)
    B = np.zeros(l)
    B = A + shift
    return (B)


# Create energy grid
def expand(Energy, Intensity,a,b):
    l = len(Energy)
    E = np.linspace(a, b, 100)
    length = len(E)
    I = np.zeros(length)
    for i in range(0, l):
        d = Energy[i] - E[0]
        index = 0
        for j in range(0, length):
            if (d > np.abs(Energy[i] - E[j])):
                index = j
                d = np.abs(Energy[i] - E[j])
#               print("*")
#        E[index] = Energy[i]
        I[index] = I[index] + Intensity[i]
        print(i)
    return (E, I)


# Load data
Active = np.loadtxt('active.dat', delimiter=',', unpack=True)
S1 = np.loadtxt('s1.dat', delimiter=',', unpack=True)             # eV
S2 = np.loadtxt('s2.dat', delimiter=',', unpack=True)               
osc1 = np.loadtxt('osc1.dat', delimiter=',', unpack=True)         # length gauge
osc2 = np.loadtxt('osc2.dat', delimiter=',', unpack=True)

#eV to a.u.
S1 = S1*0.0367
S2 = S2*0.0367


# No. of trajectories and length of each trajectory
n = len(Active[:, 0])
l = len(Active[0, :])


# Compute intensities
# everything in a.u.
intensity1 = np.zeros([n, l])
intensity2 = np.zeros([n, l])
total_steps = 0
for i in range(0, n):
    for j in range(1000, l):
        energy1 = S1[i, j]
        energy2 = S2[i, j]
        if (Active[i, j] == 1):
            intensity1[i, j] = osc1[i, j]*energy1**2
        if (Active[i, j] == 2):
            intensity2[i, j] = osc2[i, j]*energy2**2
        total_steps = total_steps + 1


# Linearize
E1 = []
E2 = []
I1 = []
I2 = []
for i in range(0, n):
    for j in range(1000, l):
        E1.append(S1[i, j])
        E2.append(S2[i, j])
        I1.append(intensity1[i, j])
        I2.append(intensity2[i, j])

E1 = np.array(E1)
E2 = np.array(E2)
I1 = np.array(I1)
I2 = np.array(I2)


# Lineshape function 
# everything in a.u.
E3, I3 = expand(E1, I1,np.min(S1),np.max(S2))    # S1 grid
E4, I4 = expand(E2, I2, np.min(S1),np.max(S2))   # S2 grid
sigma = sigma*0.0367     # eV to a.u.
Length = len(E3)
G3 = np.zeros(Length)
G4 = np.zeros(Length)
E = E3
if (ls == 'l'):
    for i in range(0, Length):
        G3 = G3 + I3[i]*(1/(np.pi))*((sigma)/((E-E3[i])**2+sigma**2))    # S1 contribution
        G4 = G4 + I4[i]*(1/(np.pi))*((sigma)/((E-E3[i])**2+sigma**2))    # S2 contribution
else:
    for i in range(0, Length):
        G3 = G3 + I3[i]*(1/(2*np.pi*sigma**2)**0.5)*np.exp(((-1)*(E-E3[i])**2)/(2*sigma**2))
        G4 = G4 + I4[i]*(1/(2*np.pi*sigma**2)**0.5)*np.exp(((-1)*(E-E3[i])**2)/(2*sigma**2))


# Final lineshape function
G = G3 + G4
G = G/(pf*total_steps)    # intensity stays in a.u.
# convert energy to eV
E = E*27.2114
# apply shift
E = apply_shift(E, shift)
# for storing final spectrum in a data file
Spectrum=np.zeros([2,Length])
Spectrum[0,:] = E
Spectrum[1,:] = G
Spectrum = np.transpose(Spectrum)

# Plot
plt.xlim(np.min(E), np.max(E))
plt.ylim(0, 1.1*np.max(G))
plt.xlabel('Energy (eV)', fontsize=12.5)
# plt.xlabel('Energy (eV)')
plt.ylabel('Photon emission rate (a.u.)', fontsize=12.5)
plt.plot(E, G, 'purple', label="Fluoresecence Spectrum")
plt.legend()
plt.savefig('Fluorescence_spectrum.png',dpi=400,bbox_inches='tight')
np.savetxt('Fluorescence_spectrum.dat', Spectrum, header="Energy (eV)   Intensity (a.u.)", fmt='%.6f')
