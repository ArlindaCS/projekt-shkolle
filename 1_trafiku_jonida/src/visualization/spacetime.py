import matplotlib.pyplot as plt
import numpy as np

def plot_space_time_diagram(history, title="Diagrami Hapësirë-Kohë"):
    """Ndërton diagramin hapësirë-kohë ku makinat dallohen si pika të zeza."""
    plt.figure(figsize=(10, 6))
    binary_matrix = np.where(history >= 0, 1, 0)
    
    plt.imshow(binary_matrix, cmap='binary', origin='upper', aspect='auto')
    plt.xlabel("Pozicioni në Rrugë")
    plt.ylabel("Hapat Kohorë (Koha)")
    plt.title(title)
    plt.grid(False)
    plt.show()

def plot_fundamental_diagram(densities, fluxes, title="Diagrami Fundamental J(rho)"):
    """Ndërton diagramin fundamental të fluksit në varësi të dendësisë."""
    plt.figure(figsize=(8, 5))
    plt.plot(densities, fluxes, 'o-', color='blue', markersize=5)
    plt.xlabel("Dendësia (rho)")
    plt.ylabel("Fluksi (J)")
    plt.title(title)
    plt.grid(True)
    plt.show()
