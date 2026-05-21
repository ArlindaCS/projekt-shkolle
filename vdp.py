# ================================
# van der Pol Oscillator Project
# Arlinda Shkina
# ================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

# --------------------------------
# Modeli van der Pol
# --------------------------------

def van_der_pol(t, y, mu):
    x, v = y

    dxdt = v
    dvdt = mu * (1 - x**2) * v - x

    return [dxdt, dvdt]

# --------------------------------
# Parametrat
# --------------------------------

mu_values = [0.5, 1, 3, 8]

t0 = 0
tf = 50

t_eval = np.linspace(t0, tf, 5000)

initial_conditions = [1, 0]

# --------------------------------
# Simulimi
# --------------------------------

for mu in mu_values:

    solution = solve_ivp(
        van_der_pol,
        [t0, tf],
        initial_conditions,
        args=(mu,),
        t_eval=t_eval
    )

    t = solution.t
    x = solution.y[0]
    v = solution.y[1]

    # --------------------------------
    # Matja e periudhes
    # --------------------------------

    peaks, _ = find_peaks(x)

    peak_times = t[peaks]

    if len(peak_times) > 1:
        periods = np.diff(peak_times)
        average_period = np.mean(periods)

        print(f"\nμ = {mu}")
        print(f"Periudha mesatare ≈ {average_period:.3f}")

    # --------------------------------
    # Grafiku x(t)
    # --------------------------------

    plt.figure(figsize=(10,5))
    plt.plot(t, x)

    plt.title(f"Van der Pol Oscillator - Time Series (μ={mu})")
    plt.xlabel("Time")
    plt.ylabel("x(t)")
    plt.grid()

    plt.show()

    # --------------------------------
    # Portreti fazor
    # --------------------------------

    plt.figure(figsize=(6,6))
    plt.plot(x, v)

    plt.title(f"Phase Portrait (μ={mu})")
    plt.xlabel("x")
    plt.ylabel("v")
    plt.grid()

    plt.show()
