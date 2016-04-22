# Script to process ozone data to make CMIP6 forcing ancillary file.

import matplotlib.pyplot as plt
import numpy as np
import iris

cubes=iris.load('/home/williamsjh/CMIP6-ozone-forcing/data-retrieval/*anwwa*jan*.pp')


