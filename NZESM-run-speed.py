# Script to plot NZESM run speeds as a function of processors decomcomposition
# and complexity.

import matplotlib.pyplot as plt
import numpy as np

processor_decomposition=[16*8,16*16,16*32]

n96=np.array([(36.*60.+59.)-(29.*60.+43.),(21.*60.+24.)-(17.*60.+1.),(28.*60.+37.)-(25.*60.+20.)])

n96_chem=n96*1.1#np.array([(.*60.+.)-(.*60.+.),(.*60.+.)-(.*60.+.),(.*60.+.)-(.*60.+.)])

n216=n96*1.2#np.array([(.*60.+.)-(.*60.+.),(.*60.+.)-(.*60.+.),(.*60.+.)-(.*60.+.)])

#'n96' is the number of seconds taken to run one day of simulation. We need to convert this to years of simulation per wallclock day.

ypd_n96=1./n96/360.*(24.*60.*60.)
ypd_n96_chem=1./n96_chem/360.*(24.*60.*60.)
ypd_n216=1./n216/360.*(24.*60.*60.)

plt.plot(processor_decomposition,ypd_n96,'-ok',ms=10)
plt.plot(processor_decomposition,ypd_n96_chem,'-sk',ms=10)
plt.plot(processor_decomposition,ypd_n216,'-^k',ms=10)
plt.xlabel('number of processors')
plt.ylabel('years $\cdot$ day $^{-1}$')
plt.grid(True)
plt.show()
