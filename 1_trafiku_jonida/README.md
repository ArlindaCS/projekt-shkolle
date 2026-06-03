# Projekti 1: Model Qelizor i Trafikut Nagel–Schreckenberg dhe Diagrami Fundamental

**Studenti:** Jonida  
**Lënda:** Modelim dhe Simulim  


##  Përshkrimi i Projektit
Ky projekt implementon një automat qelizor njëdimensional (1D Cellular Automaton) për simulimin e trafikut rrugor, bazuar në modelin klasik **Nagel–Schreckenberg (NaSch)**. Qëllimi është të studiohet formimi spontan i bllokimeve të trafikut (Traffic Jams) nga rregullat lokale të sjelljes së shoferëve, si dhe të ndërtohet diagrami fundamental që lidh fluksin e makinave me dendësinë.


traffic_cellular_automaton/
│
├── README.md
├── requirements.txt
│
├── models/
│   └── nasch.py
│
├── analysis/
│   └── traffic_metrics.py
│
├── visualization/
│   └── spacetime.py
│
├── scripts/
│   ├── run_default.py
│   └── run_parameter_scan.py
│
├── results/
│   ├── figures/
│   │   ├── spacetime_low_density.png
│   │   ├── spacetime_medium_density.png
│   │   ├── spacetime_high_density.png
│   │   └── fundamental_diagram.png
│   │
│   └── tables/
│       └── traffic_metrics.csv
│
├── tests/
│   └── test_basic_properties.py
│
├── report/
│   └── project_report.tex
│
└── notebooks/
    └── 01_exploration.ipynb

##  Si të ekzekutohet
1. Instaloni varësitë: `pip install -r requirements.txt`
2. Për diagramin hapësirë-kohë: `python scripts/run_single_density.py`
3. Për diagramin fundamental: `python scripts/scan_density.py`
