import sys
import numpy as np
import pandas as pd

participants = pd.read_csv(sys.argv[1], sep = '\t')

mean_age = participants.age.mean()

assert mean_age < 100
assert mean_age > 10 

np.savetxt("demeaned_" + sys.argv[1], participants.age-mean_age)

print("done!")
