import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import simulate_traffic
from src.analysis.traffic_metrics import get_average_velocity, calculate_flux
from src.visualization.spacetime import plot_space_time_diagram

def main():
    # Parametrat e simulimit
    L = 100            # Gjatësia e rrugës
    dendesia = 0.12    # Dendësi e ulët (provoni 0.4 për mesatare, 0.7 për të lartë)
    v_max = 5          # Shpejtësia maksimale
    p_ngadalesim = 0.3 # Probabiliteti i ngadalësimit stokastik
    hapat = 50         # Hapat kohorë
    
    print(f"Duke simuluar trafikun për dendësinë: {dendesia}...")
    history = simulate_traffic(L, dendesia, v_max, p_ngadalesim, hapat)
    
    # Llogaritja e metrikave në hapin e fundit
    rruga_fundit = history[-1]
    v_mes = get_average_velocity(rruga_fundit)
    fluksi = calculate_flux(rruga_fundit, v_mes)
    
    print("\n=== REZULTATET E SIMULIMIT ===")
    print(f"Shpejtësia mesatare finale: {v_mes:.2f}")
    print(f"Fluksi final i trafikut: {fluksi:.4f}")
    
    # Shfaqja e diagramit hapësirë-kohë
    print("\nDuke gjeneruar diagramin hapësirë-kohë...")
    plot_space_time_diagram(history, title=f"Diagrami Hapësirë-Koha (Dendësia = {dendesia})")

if __name__ == "__main__":
    main()
