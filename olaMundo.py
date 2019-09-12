#%%
print('Olá,mundo!')

#%%
import numpy as np
x = np.array([1,2,3])
x

#%%
import matplotlib.pyplot as plt
x = np.ones((50,50))
x[10:20,10:20] = 0
plt.imshow(x,cmap='gray')
plt.title('title')
plt.show()

#%%
x = np.arange(0,10,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.title('Teste')
plt.show()