iimport numpy as np

def calculate_metrics(history, burn_in_ratio=0.5):
    """
    Llogarit shpejtësinë mesatare dhe fluksin e qëndrueshëm të sistemit.
    Injoron fazën fillestare (transiente) për të shmangur gabimet në matje.
    """
    time_steps, road_length = history.shape
    start_step = int(time_steps * burn_in_ratio)
    
    # Konsiderojmë vetëm gjysmën e dytë të simulimit
    steady_state = history[start_step:]
    
    # Krijojmë një maskë booleane ku ka makina (vlera nuk është -1)
    car_mask = steady_state != -1
    total_cars_tracked = np.sum(car_mask)
    
    if total_cars_tracked == 0:
        return 0.0, 0.0, 0.0
        
    # Shpejtësia mesatare e të gjitha makinave gjatë kësaj kohe
    avg_velocity = np.sum(steady_state[car_mask]) / total_cars_tracked
    
    # Dendësia reale e matur në këtë matricë
    density = total_cars_tracked / (steady_state.shape[0] * road_length)
    
    # Formula kryesore: J = rho * <v>
    flux = density * avg_velocity
    
    return density, avg_velocity, flux
