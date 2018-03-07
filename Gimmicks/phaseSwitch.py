from pylab import *
from scipy.io import wavfile
import numpy.fft as fft
import numpy as np
from matplotlib import pyplot

#loading audiofiles
sampfrq1, tac1 = wavfile.read(r'c:\users\quirinus\desktop\a.wav')
sampfrq2, don1 = wavfile.read(r'c:\users\quirinus\desktop\b.wav')
sampfrq = sampfrq1

print('loaded')

#sample length
a = 2000000
tac2 = tac1[20000:20000+a]
don2 = don1[300000:300000+a]
print(tac2)

#extracting phase and amp

tac = fft.rfft(tac2)
tac_a = np.abs(tac)
tac_f = np.angle(tac)

print('a extracted')

don = fft.rfft(don2)
don_a = np.abs(don)
don_f = np.angle(don)

print('b extracted')

#switching phase
tac3c = fft.irfft(don_a*np.exp(tac_f*1j))//1
don3c = fft.irfft(tac_a*np.exp(don_f*1j))//1

tac3 = tac3c.astype('i2')
don3 = don3c.astype('i2')

print ('switched')

#creating new audiofiles
wavfile.write(r'c:\users\quirinus\desktop\newtac.wav', sampfrq, tac3)
wavfile.write(r'c:\users\quirinus\desktop\newdon.wav', sampfrq, don3)

#print('done')

