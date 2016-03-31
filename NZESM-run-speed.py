# Script to plot NZESM run speeds as a function of processors decomcomposition
# and complexity.

import matplotlib.pyplot as plt

processor_decomposition=[16*8,16*16,16*32]

n96=[(36*60+59)-(29*60+43),0,0]

plt.plot(processor_decomposition,n96)

plt.show()
