import matplotlib.pyplot as plt
import numpy as np

def save_spacetime_plot(history, filename, title):
    """Gjeneron dhe ruan një diagram Hapësirë-Kohë."""
    plt.figure(figsize=(10, 6))
    
    # Krijojmë një matricë binare ku makinat paraqiten me ngjyrë të zezë (1) dhe rruga e zbrazët me të bardhë (0)
    binary_matrix = np.where(history >= 0, 1, 0)
    
    plt.imshow(binary_matrix, cmap='binary', origin='upper', aspect='auto')
    plt.xlabel("Pozicioni në Rrugë (Qelizat)", fontsize=12)
    plt.ylabel("Koha (Hapat Kohorë)", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def save_fundamental_diagram(densities, results_dict, filename):
    """Ndërton diagramin fundamental J vs rho për krahasimin e probabiliteteve."""
    plt.figure(figsize=(9, 6))
    
    for p_val, fluxes in results_dict.items():
        style = 'o-' if p_val > 0 else 's--'
        label = f'p = {p_val} (Stokastik)' if p_val > 0 else 'p = 0.0 (Determinist)'
        plt.plot(densities, fluxes, style, label=label, markersize=5)
        
    plt.xlabel("Dendësia ($\rho$)", fontsize=12)
    plt.ylabel("Fluksi ($J$)", fontsize=12)
    plt.title("Diagrami Fundamental i Trafikut $J(\\rho)$", fontsize=14, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=11)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
