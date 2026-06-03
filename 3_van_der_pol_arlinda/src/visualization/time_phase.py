import matplotlib.pyplot as plt

def plot_time_series(ax, t, x, label, color):
    ax.plot(t, x, label=label, color=color)
    ax.set_xlabel('Koha (t)')
    ax.set_ylabel('Pozicioni (x)')
    ax.grid(True)
    ax.legend()

def plot_phase_portrait(ax, x, v, label, color):
    ax.plot(x, v, label=label, color=color)
    ax.set_xlabel('Pozicioni (x)')
    ax.set_ylabel('Shpejtësia (v)')
    ax.grid(True)
    ax.legend()
