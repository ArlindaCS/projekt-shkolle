import sys
import os
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.vdp import integrate_vdp
from src.analysis.period_estimation import estimate_period_and_amplitude

mu_range = np.linspace(0.1, 10.0, 50)
amplitudes = []
periods = []

for mu in mu_range:
    t, y = integrate_vdp(mu, [1.0, 1.0], (0, 100))
    period, amp = estimate_period_and_amplitude(t, y[0])
    periods.append(period)
    amplitudes.append(amp)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
fig.suptitle('Skanimi i Parametrit $\mu$', fontsize=12, fontweight='bold')

ax1.plot(mu_range, amplitudes, 'o-', color='crimson', label='Amplituda')
ax1.set_xlabel('Parametri $\mu$')
ax1.set_ylabel('Amplituda Maksimale ($x_{max}$)')
ax1.set_title('Amplituda në varësi të $\mu$')
ax1.grid(True)

ax2.plot(mu_range, periods, 'o-', color='navy', label='Periudha (T)')
ax2.set_xlabel('Parametri $\mu$')
ax2.set_ylabel('Periudha e Përafërt (T)')
ax2.set_title('Periudha në varësi të $\mu$')
ax2.grid(True)

plt.tight_layout()
plt.show()
