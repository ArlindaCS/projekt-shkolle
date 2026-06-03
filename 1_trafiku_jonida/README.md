# Projekti 1: Model Qelizor i Trafikut Nagel–Schreckenberg dhe Diagrami Fundamental

**Studenti:** Jonida Klari
---
**Lënda:** Modelim dhe Simulim  


# 🚗 Model Qelizor i Trafikut Nagel–Schreckenberg (Grupi 3)

Ky projekt është zhvilluar në kuadër të kursit **“Modelim në Fizikë”**. Qëllimi kryesor është simulimi i trafikut njëdimensional autostradal duke përdorur Automate Qelizore (Cellular Automata) dhe studimi makroskopik i formimit të bllokimeve spontane të trafikut (*phantom traffic jams*).

---

## 🎯 Qëllimi Shkencor
Projekti synon të rikrijojë tranzicionin e fazës në trafikun rrugor: nga një **regjim i rrjedhës së lirë** (ku makinat lëvizin me shpejtësi maksimale) në një **regjim të bllokuar** (ku krijohen valë bllokimi që propagandojnë mbrapsht në raport me lëvizjen e makinave). Përmes skanimit të parametrave, ndërtohet *Diagrami Fundamental* i cili lidh densitetin e makinave me fluksin e përgjithshëm të sistemit.

---

## 📐 Ekuacionet Kryesore dhe Rregullat e Modelit

Modeli Nagel-Schreckenberg (NaSch) është një model diskret hapësirë-kohë. Rruga ndahet në qeliza me gjatësi $L$. Çdo qelizë ose është e zbrazët, ose përmban një makinë të vetme me shpejtësi $v \in \{0, 1, \dots, v_{max}\}$.

Në çdo hap kohor $t \rightarrow t+1$, shpejtësia $v_i$ dhe pozicioni $x_i$ i çdo makine përditësohen në mënyrë sinkrone sipas 4 rregullave të mëposhtme:

1. **Përshpejtimi:** Shoferët tentojnë të ecin sa më shpejt të jetë e mundur.
   $$v_i \leftarrow \min(v_i + 1, v_{max})$$

2. **Frenimi (Shmangia e përplasjes):** Shpejtësia kufizohet nga distanca me makinën përpara ($g_i = x_{next} - x_i - 1$).
   $$v_i \leftarrow \min(v_i, g_i)$$

3. **Ngadalësimi Stokastik:** Modelon vonesat psikologjike të shoferëve apo frenimet e rastësishme. Me një probabilitet $p$:
   $$v_i \leftarrow \max(v_i - 1, 0)$$

4. **Lëvizja Fizike:** Makinat zhvendosen përpara në rrjetë sipas kushteve periodike kufitare (unazë e mbyllur).
   $$x_i \leftarrow (x_i + v_i) \pmod L$$

### Metrikat Makroskopike
- **Dendësia ($\rho$):** $\rho = \frac{N}{L}$, ku $N$ është numri i makinave.
- **Shpejtësia Mesatare ($\langle v \rangle$):** Llogaritet në gjendje të qëndrueshme për të gjitha makinat.
- **Fluksi ($J$):** Sasia e makinave që kalojnë në një pikë për njësi kohe:
   $$J = \rho \langle v \rangle$$

---

## 📁 Struktura e Repozitorit

```text
traffic_cellular_automaton/
├── README.md                     # Ky dokumentim
├── requirements.txt              # Libraritë e nevojshme (numpy, matplotlib)
├── src/
│   ├── __init__.py
│   ├── models/
│   │   └── nasch.py              # Logjika e Automatit Qelizor
│   ├── analysis/
│   │   └── traffic_metrics.py    # Llogaritja e fluksit dhe shpejtësisë
│   └── visualization/
│   │   └── spacetime.py          # Moduli për gjenerimin e grafikëve
├── scripts/
│   ├── run_single_density.py     # Ekzekutimi për një dendësi të vetme
│   └── scan_density.py           # Skanimi i parametrave (Diagrami Fundamental)
├── tests/
│   └── test_basic_properties.py  # Teste automatike për ruajtjen e makinave
└── results/
    ├── figures/                  # Grafikët PNG të gjeneruar
    └── tables/                   # Metrikat numerike në format tekstirequirements.txt`
2. Për diagramin hapësirë-kohë: `python scripts/run_single_density.py`
3. Për diagramin fundamental: `python scripts/scan_density.py`
