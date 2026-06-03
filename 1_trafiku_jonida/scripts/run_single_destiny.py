import os
import sys
# Shton direktorinë rrënjë në mënyrë që Python të gjejë modulin src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.nasch import NaSchModel
from src.visualization.spacetime import save_spacetime_plot

# Krijojmë dosjen e figurave nëse nuk ekziston
os.makedirs('results/figures', exist_ok=True)

scenarios = {
    "low": {"density": 0.1, "title": "Dendësi e Ulët (rho=0.1) - Rrjedhë e Lirë"},
    "medium": {"density": 0.3, "title": "Dendësi Mesatare (rho=0.3) - Formim Bllokimesh"},
    "high": {"density": 0.7, "title": "Dendësi e Lartë (rho=0.7) - Bllokim i Plotë"}
}

for name, params in scenarios.items():
    model = NaSchModel(road_length=150, density=params["density"], max_velocity=5, p_slow=0.3)
    history = model.simulate(time_steps=120)
    
    output_path = f"results/figures/spacetime_{name}.png"
    save_spacetime_plot(history, output_path, params["title"])
    print(f"Grafiku u ruajt: {output_path}")
