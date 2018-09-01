import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


hist = pd.Series(np.random.randint(0, 7, size=6))
print("Histogram:\n", hist)
print("value_counts():\n", hist.value_counts())
plt.hist(hist, color='purple')
plt.show()