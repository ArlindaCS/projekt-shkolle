import numpy as np
from scipy.integrate import solve_ivp

def van_der_pol(t, y, mu):
    """Përkufizon sistemin e ekuacioneve të Oshilatorit Van der Pol."""
    x, v = y
    dxdt = v
    dvdt = mu * (1 - x**2) * v - x
    return [dxdt, dvdt]

def integrate_vdp(mu, y0, t_span, t_eval=None):
    """Integron ekuacionin për një kusht fillestar y0 = [x0, v0]."""
    if t_eval is None:
        t_eval = np.linspace(t_span[0], t_span[1], 2500)
    
    sol = solve_ivp(van_der_pol, t_span, y0, args=(mu,), t_eval=t_eval, method='RK45')
    return sol.t, sol.y
