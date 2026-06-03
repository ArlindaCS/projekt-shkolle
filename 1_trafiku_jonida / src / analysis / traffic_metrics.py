import numpy as np

def calculate_density(road):
    """Llogarit dendësinë rho (numri i makinave / gjatësia e rrugës)."""
    if len(road) == 0:
        return 0.0
    # Makinat shënohen me numra >= 0 (shpejtësitë), ndërsa -1 tregon hapësirë bosh
    num_cars = np.sum(road >= 0)
    return float(num_cars / len(road))

def calculate_flux(road, average_velocity):
    """Llogarit fluksin e trafikut J = rho * v_mesatare."""
    rho = calculate_density(road)
    return float(rho * average_velocity)

def get_average_velocity(road):
    """Llogarit shpejtësinë mesatare të makinave që janë aktualisht në rrugë."""
    cars_velocities = road[road >= 0]
    if len(cars_velocities) == 0:
        return 0.0
    return float(np.mean(cars_velocities))
