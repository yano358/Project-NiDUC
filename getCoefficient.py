from rng import random_value as rd

# Only used for uniform value
import random as unif

def GenerateCoeff():
    final = 0
    if rd(37, 10, 0, 10, integer=True) >= 8:
        final = unif.uniform(-1,1)*2
        return final
    else:
        return final
