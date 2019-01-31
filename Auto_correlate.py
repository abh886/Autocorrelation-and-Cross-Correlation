# -*- coding: utf-8 -*-
"""
ACF and CCF
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

a=[1,2,3,4]

b=[5,4,3,2]

m=np.correlate(a,a,mode='full')

#Expected values  4 11 20 30 20 11  4

rxy=correlate(a,b,mode='full')

ryx=correlate(b,a,mode='full')


#l=np.linspace(-4,4)

plt.stem(m)
plt.title('ACF')
plt.xlabel('time lag')
plt.ylabel('amplitude')
plt.show()

print(m)

plt.stem(rxy)
plt.title('CCF')
plt.xlabel('time lag')
plt.ylabel('Amplitude')
plt.show()
#Expected values 2  7 16 30 34 31 20

plt.stem(ryx)
plt.title('CCF')
plt.xlabel('time lag')
plt.ylabel('Amplitude')
plt.show()

#Expected values 20 31 34 30 16  7  2