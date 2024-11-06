import pandas as pd
import numpy as np

num_dict = {'x' : [4, 9], 'y' : [16, 25 ]}
df = pd.DataFrame(num_dict)
print(df)
print(df.applymap(np.sqrt))