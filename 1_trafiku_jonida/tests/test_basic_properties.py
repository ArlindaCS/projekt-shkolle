import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import NaSchModel

def test_conservation_of_cars():
    """Teston nëse numri i makinave mbetet konstant gjatë simulimit."""
    model = NaSchModel(road_length=100, density=0.2, max_velocity=5, p_slow=0.3)
    initial_cars = model.N
    
    # Ekzekutojmë 50 hapa
    history = model.simulate(time_steps=50)
    
    for t in range(50):
        current_cars = sum(1 for x in history[t] if x != -1)
        assert current_cars == initial_cars, f"Gabim në hapin {t}: Makinat nuk ruhen!"
    
    print("Testi i Ruajtjes së Makinave: KALUAR SUKSESSHËM!")

if __name__ == "__main__":
    test_conservation_of_cars()
