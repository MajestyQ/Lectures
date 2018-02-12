import numpy as np
from numpy import exp, pi, sqrt
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from scipy import signal

#Auslesen der Messdaten
data = np.genfromtxt (r'C:\Users\Quirinus\Documents\GitHub\Praktikum\Praktikum\232 - Michelson Interferometer\Interferenz_Daten.csv', delimiter = ",", 
                     skip_header = 7300, skip_footer = 5500, usecols = (0, 1))
x1 = data[0:, 0]
y1 = data[0:, 1]

#Da um 0.2 sehr starkes "rauschen" der Messwerte zu sehen ist wurde, werden diese Werte beim fitten der GauÃŸkurve inoriert
mask1 = (y1>0.02)

y2 = y1[mask1]
x2 = x1[mask1]

#Besimmen der lokalen Maxima
mask2 = argrelextrema(y2, np.greater_equal, order = 1)
y3 = y2[mask2]
x3 = x2[mask2]

#Fitten der GauÃŸkurve
def gaussian(x, mu, sigma, A): 
    return A / (sigma * sqrt(2 * pi)) * exp(-(x - mu)**2 / sigma**2 / 2)
p = [0.01, 0.01, 0.01]
popt, pcov = curve_fit(gaussian, x3, y3, p0 = p)
 

#plotten der Messdaten
plt.plot(x1, y1, linewidth = 0.1, color = 'k', linestyle = '--')

#plotten des Fits
x = np.linspace(x1[0],x1[-1], 1000)
plt.plot(x, gaussian(x, *popt), 'r-', linewidth = 1)
plt.legend(['Messwerte', 'Gauß-Fit'])
plt.xlabel('Zeit in s')
plt.ylabel('Intensität')
plt.title('Keine Ahnung was ich getan hab')

#speichern des Graphen
plt.savefig(r'C:\Users\Quirinus\Desktop\plot1.pdf', figsize = 'a4')



