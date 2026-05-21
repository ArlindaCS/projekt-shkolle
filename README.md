# Van der Pol Oscillator – Ciklet Limit dhe Skanimi i Parametrit μ

## Përshkrimi i projektit
Ky projekt modelon dhe simulon oshilatorin jolinear të Van der Pol duke përdorur Python. Qëllimi është të studiohet sjellja e sistemit, formimi i cikleve limit dhe ndikimi i parametrit μ në dinamikën e sistemit.


## Modeli matematikor

Ekuacioni i Van der Pol:

d²x/dt² − μ(1 − x²) dx/dt + x = 0

Forma sistem:

dx/dt = v  
dv/dt = μ(1 − x²)v − x


## Qëllimi
- Simulimi i një sistemi jolinear oscilues
- Analiza e cikleve limit
- Studimi i ndikimit të parametrit μ
- Matja e periudhës së lëkundjeve
- Vizualizimi i portreteve fazore dhe grafikëve kohorë


## Metodat e përdorura
- Integrimi numerik me `solve_ivp`
- Analizë e sinjalit me `find_peaks`
- Grafikë me `matplotlib`
- NumPy për llogaritje numerike


## Struktura e projektit

van_der_pol_limit_cycle/

- src/
- scripts/
- results/
- notebooks/
- README.md
- requirements.txt


## Si ta ekzekutosh

Në terminal:

pip install numpy scipy matplotlib

python run_vdp.py


## Rezultatet
- Sistemi konvergon në cikël limit stabil
- Amplituda dhe forma varen nga μ
- Periudha ndryshon me rritjen e μ


## Autorët
- Jonida Klari – Modeli i trafikut
- Alda Xhika – Renditja e artikujve
- Arlinda Shkina – Van der Pol oscillator, ciklet limit dhe analiza e periudhës

## Përfundim
Ky projekt demonstron sjelljen jolineare të një sistemi fizik dhe rëndësinë e simulimeve numerike në analizën e fenomeneve dinamike.
