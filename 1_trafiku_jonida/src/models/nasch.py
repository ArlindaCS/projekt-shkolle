import numpy as np

def initialize_road(length, density, max_velocity):
    """Krijon strukturën e rrugës dhe gjendjen fillestare të makinave."""
    road = -1 * np.ones(length, dtype=int)
    num_cars = int(length * density)
    available_positions = np.random.choice(length, num_cars, replace=False)
    for pos in available_positions:
        road[pos] = np.random.randint(0, max_velocity + 1)
    return road

def get_distance(road, pos):
    """Llogarit distancën deri te makina tjetër përpara (kushte periodike)."""
    length = len(road)
    distance = 0
    for i in range(1, length):
        next_pos = (pos + i) % length
        if road[next_pos] != -1:
            return distance
        distance += 1
    return length - 1

def step_nagel_schreckenberg(road, max_velocity, p_slowdown):
    """Zbaton 4 rregullat: përshpejtim, frenim, ngadalësim, lëvizje."""
    length = len(road)
    new_road = -1 * np.ones(length, dtype=int)
    
    for pos in range(length):
        v = road[pos]
        if v == -1:
            continue
        if v < max_velocity:
            v += 1
        d = get_distance(road, pos)
        if v > d:
            v = d
        if v > 0 and np.random.rand() < p_slowdown:
            v -= 1
        new_pos = (pos + v) % length
        new_road[new_pos] = v
    return new_road

def simulate_traffic(length, density, max_velocity, p_slowdown, steps):
    """Simulon trafikun për një numër të caktuar hapash kohorë."""
    road = initialize_road(length, density, max_velocity)
    history = [road.copy()]
    for _ in range(steps):
        road = step_nagel_schreckenberg(road, max_velocity, p_slowdown)
        history.append(road.copy())
    return np.array(history)
