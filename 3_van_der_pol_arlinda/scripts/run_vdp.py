import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.vdp import integrate_vdp
from src.visualization.time_phase import plot_time_series, plot_phase_portrait

mu_values = [0.5, 1, 3, 8]
t_span = (0, 50)

initial_conditions = [
    {'y0': [0.1, 0.1], 'label': 'Fillimi: [0.1, 0.1] (Brenda)', 'color': 'blue'},
    {'y0': [4.0, 4.0], 'label': 'Fillimi: [4.0, 4.0] (Jashtë)', 'color': 'orange'}
]

for mu in mu_values:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
    fig.suptitle(f'Oshilatori Van der Pol për $\mu$ = {mu}', fontsize=12, fontweight='bold')
    
    for cond in initial_conditions:
        t, y = integrate_vdp(mu, cond['y0'], t_span)
        plot_time_series(ax1, t, y[0], cond['label'], cond['color'])
        plot_phase_portrait(ax2, y[0], y[1], cond['label'], cond['color'])
        
    ax1.set_title('Seria Kohore $x(t)$')
    ax2.set_title('Portreti Fazor ($v$ vs $x$)')
    plt.tight_layout()
    plt.show()
