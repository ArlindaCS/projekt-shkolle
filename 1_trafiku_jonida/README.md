# Projekti 1: Model Qelizor i Trafikut Nagel–Schreckenberg dhe Diagrami Fundamental

**Studenti:** Jonida  
**Lënda:** Modelim dhe Simulim  


##  Përshkrimi i Projektit
Ky projekt implementon një automat qelizor njëdimensional (1D Cellular Automaton) për simulimin e trafikut rrugor, bazuar në modelin klasik **Nagel–Schreckenberg (NaSch)**. Qëllimi është të studiohet formimi spontan i bllokimeve të trafikut (Traffic Jams) nga rregullat lokale të sjelljes së shoferëve, si dhe të ndërtohet diagrami fundamental që lidh fluksin e makinave me dendësinë.


##  Rregullat Lokale të Modelit
Në çdo hap kohor, shpejtësia e çdo makine përditësohet sipas katër hapave:
1. **Përshpejtim:** $v \leftarrow \min(v + 1, v_{\max})$
2. **Frenim nga distanca:** $v \leftarrow \min(v, d)$
3. **Ngadalësim stokastik:** $v \leftarrow \max(v - 1, 0)$ (me probabilitet $p$)
4. **Lëvizje:** $x \leftarrow (x + v) \pmod L$


##  Struktura e Skedarëve
- `src/models/nasch.py`: Logjika e rregullave dhe simulimi.
- `src/analysis/traffic_metrics.py`: Llogaritja e metrikave (fluksi, dendësia).
- `src/visualization/spacetime.py`: Gjenerimi i diagrameve.
- `scripts/`: Skriptet për ekzekutim (`run_single_density.py` dhe `scan_density.py`).


##  Si të ekzekutohet
1. Instaloni varësitë: `pip install -r requirements.txt`
2. Për diagramin hapësirë-kohë: `python scripts/run_single_density.py`
3. Për diagramin fundamental: `python scripts/scan_density.py`
