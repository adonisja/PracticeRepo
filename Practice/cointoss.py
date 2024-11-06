import numpy as np
np.random.seed(123)
coin = np.random.randint(0,2)
print(coin, end=': ')
if coin:
    print("Tails")
else:
    print("Heads")
