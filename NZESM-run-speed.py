# Script to plot NZESM run speeds as a function of processors decomcomposition
# and complexity.

import matplotlib.pyplot as plt
import numpy as np

processor_decomposition=[16*8,16*16,16*32]

n96=np.array([(36.*60.+59.)-(29.*60.+43.),(21.*60.+24.)-(17.*60.+1.),(28.*60.+37.)-(25.*60.+20.)])

print(n96)

#'n96' is the number of seconds taken to run one day of simulation. We need to convert this to years of simulation per wallclock day.

ypd=(np.divide(np.divide(1.,n96),360./(24*60*60)))

print(ypd)

plt.plot(processor_decomposition,ypd,'-o')

plt.show()
