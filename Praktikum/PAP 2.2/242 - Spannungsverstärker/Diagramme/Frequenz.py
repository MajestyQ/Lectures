import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')

frq = np.array([0.2, 0.4, 0.8, 2, 4, 8, 20, 40, 80, 150, 200, 300])
rg1 = np.array([19.2, 19.0, 18.8, 17.0, 13.6, 8.4, 3.6, 1.88, 1, 0.512, 0.384, 0.260])
rg2 = np.array([7.36, 7.36, 7.36, 7.2, 6.88, 5.68, 3.32, 1.84, 0.944, 0.512, 0.380, 0.256])
rg3 = np.array([1.28, 1.28, 1.28, 1.28, 1.28, 1.26, 1.22, 1.06, 0.760, 0.472, 0.364, 0.248])
rg4 = np.array([1.28, 1.28, 1.28, 1.22, 1.09, 0.8, 0.388, 0.204, 0.101, 0.0544, 0.0416, 0.0278])

frq1 = np.array([0.3, 0.4, 0.5, 0.65, 0.8, 1, 3, 5, 7, 9, 10, 14, 20])
rg3p = np.array([0.364, 0.464, 0.552, 0.664, 0.784, 0.880, 1.26, 1.3, 1.32, 1.32, 1.32, 1.32, 1.28])

plt.figure(2)
plt.ylabel('Verstärkung')
plt.xlabel('Frequenz'+'$[1/s]$')
plt.xscale('log')
plt.yscale('log')
plt.plot(frq, rg1, label = 'RG1', marker = 'x', markersize = '3')
plt.plot(frq, rg2, label = 'RG2', marker = 'x', markersize = '3')
plt.plot(frq, rg3, label = 'RG3', marker = 'x', markersize = '3')
plt.plot(frq, rg4, label = 'RG4', marker = 'x', markersize = '3')
plt.plot(frq1, rg3p, label = 'RG4 mit Kondensator', marker = 'x', markersize = '3')
plt.legend(frameon = True)
plt.tight_layout()
plt.savefig('Frequenzen.pdf')

