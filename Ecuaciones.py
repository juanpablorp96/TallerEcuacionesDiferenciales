import numpy as np
def forward_euler():
    h = 0.1
    num_steps = 10

    x = np.zeros([num_steps + 1, 2]) # paso
    y = np.zeros([num_steps + 1, 2])
    z = np.zeros([num_steps + 1, 2])


    z[0, 0] = 2. # condicion inicial
    z[0, 0] = 2.

    y[0, 1] = 1.  # condicion inicial
    y[0, 1] = 1.

    for step in range(num_steps):
        z[step + 1] = z[step] + h * (-x[step] + y[step] - z[step])
        y[step + 1] = y[step] + h * (x[step] + y[step] + z[step])

    return z, y
    
    
print(forward_euler())