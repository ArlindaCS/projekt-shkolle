# Vizualizimi
# Diagrami hapësirë-kohë dhe ai fundamental.

import matplotlib.pyplot as plt

def save_spacetime(history, filename):
    plt.figure(figsize=(10, 8))
    plt.imshow(history, cmap='binary', aspect='auto')
    plt.xlabel("Hapësira")
    plt.ylabel("Koha")
    plt.savefig(filename)
    plt.close()

def save_fundamental(densities, flows, labels, filename):
    plt.figure(figsize=(8, 6))
    for d, f, l in zip(densities, flows, labels):
        plt.plot(d, f, 'o-', label=f"p={l}")
    plt.xlabel("Dendësia (rho)")
    plt.ylabel("Fluksi (J)")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
