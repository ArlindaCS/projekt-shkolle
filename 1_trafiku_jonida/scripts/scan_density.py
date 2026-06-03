import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import simulate_traffic
from src.analysis.traffic_metrics import get_average_velocity, calculate_flux, calculate_density
from src.visualization.spacetime import plot_fundamental_diagram

def run_density_scan(p_slowdown):
    L = 100
    v_max = 5
    hapat = 100
    
    # Skanojmë dendësitë nga 0.03 deri në 0.95
    input_densities = np.linspace(0.03, 0.95, 30)
    measured_densities = []
    measured_fluxes = []
    
    for d in input_densities:
        history = simulate_traffic(L, d, v_max, p_slowdown, hapat)
        # Marrim mesataren e 20 hapave të fundit për të qenë në gjendje të stabilizuar
        history_fundit = history[-20:]
        
        flux_steps = []
        density_steps = []
        for rruga in history_fundit:
            v_mes = get_average_velocity(rruga)
            flux_steps.append(calculate_flux(rruga, v_mes))
            density_steps.append(calculate_density(rruga))
            
        measured_densities.append(np.mean(density_steps))
        measured_fluxes.append(np.mean(flux_steps))
        
    return measured_densities, measured_fluxes

def main():
    print("Duke filluar skanimin e dendësive për Diagramin Fundamental...")
    
    # Skanimi për rastin stokastik (p = 0.3)
    print("1. Duke kalkuluar rastin stokastik (p=0.3)...")
    rho_stokastik, j_stokastik = run_density_scan(p_slowdown=0.3)
    
    # Shfaqja e Diagramit Fundamental për Jonidën
    plot_fundamental_diagram(rho_stokastik, j_stokastik, title="Diagrami Fundamental J(rho) - Modeli Nagel-Schreckenberg")

if __name__ == "__main__":
    main()
