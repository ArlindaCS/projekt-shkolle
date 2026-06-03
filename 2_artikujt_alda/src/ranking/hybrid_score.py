import datetime

def calculate_freshness(year, current_year=2026):
    """Llogarit faktorin e freskisë që favorizon artikujt më të rinj."""
    age = current_year - year
    if age < 0:
        age = 0
    # Një model zbutjeje (decay) eksponencial ose linear i thjeshtë
    return math.exp(-0.2 * age)

def compute_hybrid_scores(articles, relevance_scores, pagerank_scores, weights, current_year=2026):
    """Kombinon komponentët e normalizuar në një pikë të vetme hibride."""
    w_B, w_P, w_F = weights
    hybrid_results = []
    
    # Gjejmë vlerat maksimale për normalizim në [0, 1]
    max_B = max(relevance_scores.values()) if relevance_scores and max(relevance_scores.values()) > 0 else 1.0
    max_P = max(pagerank_scores.values()) if pagerank_scores and max(pagerank_scores.values()) > 0 else 1.0
    
    for art in articles:
        art_id = art['id']
        
        # Normalizimi
        B_i = relevance_scores.get(art_id, 0.0) / max_B
        P_i = pagerank_scores.get(art_id, 0.0) / max_P
        F_i = calculate_freshness(art['year'], current_year)
        
        # Formula hibride e kërkuar
        score = w_B * B_i + w_P * P_i + w_F * F_i
        
        hybrid_results.append({
            'id': art_id,
            'title': art['title'],
            'year': art['year'],
            'final_score': score,
            'details': {'relevance': B_i, 'pagerank': P_P_i if 'P_i' else P_i, 'freshness': F_i}
        })
        
    # Renditja nga më i larti tek më i ulëti
    hybrid_results.sort(key=lambda x: x['final_score'], reverse=True)
    return hybrid_results
