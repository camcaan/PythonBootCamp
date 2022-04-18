import pandas as pd
s=pd.Series([1,3,5,np.nan,6,8])
print(s)


import matplotlib as plt
x = np.arange(0,3 * np.pi, 0.1)
y= np.sin(x)

plt.plot(x,y)
plt.show()