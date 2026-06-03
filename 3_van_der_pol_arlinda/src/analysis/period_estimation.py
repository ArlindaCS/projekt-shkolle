import numpy as np

def estimate_period_and_amplitude(t, x, burn_in=0.5):
    """Estimon periudhën dhe amplitudën e ciklit limit."""
    start_idx = int(len(t) * burn_in)
    t_stable = t[start_idx:]
    x_stable = x[start_idx:]
    
    amplitude = np.max(x_stable)
    zero_crossings = []
    for i in range(1, len(x_stable)):
        if x_stable[i-1] < 0 <= x_stable[i]:
            t_zero = t_stable[i-1] - x_stable[i-1] * (t_stable[i] - t_stable[i-1]) / (x_stable[i] - x_stable[i-1])
            zero_crossings.append(t_zero)
            
    if len(zero_crossings) < 2:
        return None, amplitude
        
    periods = np.diff(zero_crossings)
    return np.mean(periods), amplitude
