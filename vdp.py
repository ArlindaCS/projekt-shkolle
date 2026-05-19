import numpy as np
from scipy.integrate import solve_ivp

from src.models.vdp import van_der_pol
from src.analysis.period_estimation import estimate_period

mu_values = [0.5, 1, 3, 8]

for mu in mu_values:

    t_span = (0, 80)
    t_eval = np.linspace(0, 80, 8000)

    initial_conditions = [1, 0]

    solution = solve_ivp(
        van_der_pol,
        t_span,
        initial_conditions,
        t_eval=t_eval,
        args=(mu,)
    )

    t = solution.t
    x = solution.y[0]

    amplitude = np.max(np.abs(x))
    period = estimate_period(t, x)

    print(f"\nmu = {mu}")
    print(f"Amplitude ≈ {amplitude}")
    print(f"Period ≈ {period}") 
