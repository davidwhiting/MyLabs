## Code for Volume 1 Problem 1
##
import numpy as np
from matplotlib import pyplot as plt

import LinearTransform

LT = LinearTransform("data/horse.npy")
LT.plot()
LT.stretch(0.5, 2).plot()
## The reset could be made automatically
LT.reset().shear(0.5, horizontal=True).plot()
LT.reset().reflection(0, 1).plot()