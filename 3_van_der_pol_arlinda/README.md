# Projekt Grupi - Modelimi Numerik dhe Simulimi Computational

## Anëtarët e Grupit dhe Temat
Ky repozitor përmban projektet e përbashkëta për kursin tonë akademik, të ndara sipas roleve orientuese të secilit anëtar:

1. **Jonida Klari** - Drejtuese e modelit të trafikut; përgjegjëse për automatin qelizor.
2. **Alda Xhika** - Drejtuese e renditjes së artikujve; përgjegjëse për relevancën tekstuale.
3. **Arlinda Shkina** - Drejtuese e Van der Pol; përgjegjëse për ciklet limit dhe matjen e periudhës.

---

## Pjesa 3: Oshilatori Van der Pol (Arlinda Shkina)

### 1. Përshkrimi Teorik i Modelit
Oshilatori Van der Pol është një model klasik i sistemeve dinamike jolineare me fërkim (dampim) jolinear. Ai përshkruhet nga ekuacioni diferencial i rendit të dytë:

$$\frac{d^2x}{dt^2} - \mu(1 - x^2)\frac{dx}{dt} + x = 0$$

Ku:
* $x$ është pozicioni i sistemit.
* $\mu$ është një parametër skalar që rregullon shkallën e jolinearitetit dhe fërkimit.

Për ta zgjidhur në mënyrë numerike, ky ekuacion zbërthehet në një sistem prej dy ekuacionesh diferenciale të rendit të parë:
1. $\frac{dx}{dt} = v$
2. $\frac{dv}{dt} = \mu(1 - x^2)v - x$

### 2. Karakteristikat e Ciklit Limit
Veçantia kryesore e Oshilatorit Van der Pol është ekzistenca e një **Cikli Limit** të qëndrueshëm. Pavarësisht nëse sistemi fillon me kushte fillestare brenda apo jashtë këtij cikli, të gjitha trajektoret në portretin fazor ($v$ vs $x$) konvergjojnë drejt së njëjtës trajektore të mbyllur:
* Për vlera të vogla të $\mu$ ($\mu \to 0$), cikli limit është pothuajse rrethor (lëkundje harmonike).
* Për vlera të mëdha të $\mu$ ($\mu \gg 1$), sistemi kthehet në një *oshilator relaksimi*, ku sistemi lëviz ngadalë në disa faza dhe kërcen shpejt në faza të tjera.

### 3. Struktura e Kodit (Arkitektura Modulare)
Kodi është organizuar në folderin `3_van_der_pol_arlinda/`
```text
3_van_der_pol_arlinda/
├── README.md                  # Dokumentacioni i projektit
├── requirements.txt           # Libraritë e nevojshme (numpy, scipy, matplotlib)
├── src/
│   ├── models/
│   │   └── vdp.py             # Përkufizimi matematikor dhe integrimi me RK45
│   ├── analysis/
│   │   └── period_estimation.py # Algoritmi për llogaritjen e periudhës dhe amplitudës
│   └── visualization/
│       └── time_phase.py      # Funksionet për ndërtimin e grafikëve
├── scripts/
│   ├── run_default.py         # Simulimi kryesor për mu = 0.5, 1, 3, 8
│   └── run_parameter_scan.py  # Skanimi i parametrit mu (0.1 deri 10.0)
├── notebooks/
│   └── 01_exploration.ipynb   # Faza e eksplorimit fillestar (Google Colab)
└── results/
    └── figures/               # Direktoria për ruajtjen e grafikëve të gjeneruar
