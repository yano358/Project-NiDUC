from rng import random_value as rd

#only used for uniform value 
import random as unif

def GenerateCoeff():
    final = 0
    if rd(10) >= 8:
        final = unif.uniform(-1,1)*2
        return final
    else:
        return final
