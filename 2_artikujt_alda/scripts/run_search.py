import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.text.relevance.import compute_relevance # rregulluar path-i sipas kodit
from src.text.relevance import compute_relevance
from src.ranking.citation_pagerank import compute_pagerank
from src.ranking.hybrid_score import compute_hybrid_scores

def load_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, '../examples/articles.json')
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    articles = load_data()
    query = "quantum computing physics"
    print(f"Kërkimi për fjalët: '{query}'\n" + "="*40)
    
    # 1. Llogaritja e relevancës tekstuale (B)
    relevance_scores = {art['id']: compute_relevance(query, art) for art in articles}
    
    # 2. Llogaritja e PageRank (P)
    pagerank_scores = compute_pagerank(articles)
    
    # 3. Skanimi i peshave (Eksperimenti minimal)
    # Skenari A: Fokus te Teksti dhe Autoriteti (pa freski)
    weights_A = (0.6, 0.4, 0.0)
    # Skenari B: Fokus te Artikujt e Rinj (me freski të lartë)
    weights_B = (0.4, 0.2, 0.4)
    
    for emri, peshat in [("Skenari A (Pa Freski)", weights_A), ("Skenari B (Me Freski të lartë)", weights_B)]:
        print(f"\n--- {emri} [w_B={peshat[0]}, w_P={peshat[1]}, w_F={peshat[2]}] ---")
        results = compute_hybrid_scores(articles, relevance_scores, pagerank_scores, peshat)
        
        for i, res in enumerate(results[:10], start=1):
            print(f"{i}. {res['title']} ({res['year']}) - Pikët Totale: {res['final_score']:.4f}")
            print(f"   [Tekst: {res['details']['relevance']:.2f}, PR: {res['details']['pagerank']:.2f}, Freski: {res['details']['freshness']:.2f}]")

if __name__ == "__main__":
    main()
