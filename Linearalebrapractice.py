import numpy as np
import matplotlib.pyplot as plt
t= np.linspace(0,40,1000)

d_r = 2.5*t

d_s = 3.5*(t-5)

fig, ax = plt.subplots()
plt.title("A bank robber Caught")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")  
ax.set_xlim(0, 40)
ax.set_ylim(0, 100)

ax.plot(t, d_r, label="Robber", color='red')
ax.plot(t, d_s, label="Police", color='blue')   
plt.axvline(x=30,color='purple', linestyle='--', label='Police arrives')

_ = plt.axhline(y=87.5, color='green', linestyle='--', label='Robber caught')
plt.legend()
plt.show()