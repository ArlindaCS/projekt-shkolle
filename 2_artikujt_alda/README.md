# Projekti 2: Renditja e Artikujve Shkencorë me BM25 të Thjeshtuar, PageRank dhe Freski

**Studenti:** Alda Xhika  
**Lënda:** Modelim dhe Simulim  

---

## 📌 Përshkrimi i Projektit
Ky projekt implementon një motor kërkimi të thjeshtuar dhe analitik për artikujt shkencorë. Qëllimi është të ndërtohet një sistem hibrid renditjeje (Ranking System) që kombinon përputhjen tekstuale të pyetjes (Query), autoritetin e artikullit në rrjetin e citimeve dhe faktorin kohor të freskisë.

Sistemi integron tre shtylla kryesore metodologjike:
1. **Relevanca Tekstuale ($B_i$):** Analizon titullin dhe abstraktin e artikullit duke llogaritur frekuencën e fjalëve (një model i thjeshtuar TF-IDF / BM25).
2. **PageRank ($P_i$):** Përdor teorinë e grafeve për të llogaritur rëndësinë strukturore të një artikulli bazuar në rrjetin e citimeve.
3. **Freskia ($F_i$):** Një funksion zbutës eksponencial ($e^{-\alpha \cdot t}$) që favorizon artikujt e publikuar rishtazi.

---

## 📐 Modelimi Matematik (Formula Hibride)

Renditja përfundimtare e artikujve bëhet sipas kombinimit linear të komponentëve të normalizuar në rrezen $[0, 1]$:

$$S_i = w_B B_i + w_P P_i + w_F F_i$$

Ku peshat menaxhohen nën kushtin:
$$w_B + w_P + w_F = 1.0$$

---

## 📂 Struktura e Skedarëve të Projektit

Projekti është organizuar në mënyrë modulare sipas udhëzimeve akademike:

```text
2_artikuj_alda/
├── README.md               # Ky dokument udhëzues dhe shpjegues
├── requirements.txt        # Libraritë e jashtme të nevojshme (numpy)
├── examples/
│   └── articles.json       # Dataseti shembull me artikuj shkencorë
├── src/
│   ├── text/
│   │   └── relevance.py    # Algoritmi i tokenizimit dhe llogaritjes së TF
│   └── ranking/
│       ├── citation_pagerank.py  # Ndërtimi i matricës dhe iterimet e PageRank
│       └── hybrid_score.py       # Llogaritja e freskisë dhe formula përfundimtare
└── scripts/
    └── run_search.py       # Skripti kryesor i ekzekutimit dhe skanimit të peshave
