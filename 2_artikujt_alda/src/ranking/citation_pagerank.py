import numpy as np

def compute_pagerank(articles, d=0.85, num_iter=20):
    """Llogarit pikët PageRank bazuar në rrjetin e citimeve të artikujve."""
    N = len(articles)
    if N == 0:
        return {}
        
    # Krijojmë matricën e fqinjësisë (Adjacency Matrix)
    adj_matrix = np.zeros((N, N))
    id_to_idx = {art['id']: i for i, art in enumerate(articles)}
    
    for i, art in enumerate(articles):
        for citation in art.get('citations', []):
            if citation in id_to_idx:
                # Artikulli 'citation' citon artikullin 'art['id']'
                adj_matrix[id_to_idx[citation]][i] = 1

    # Rregullimi i nyjeve pa lidhje dalëse (Dangling nodes)
    out_degrees = np.sum(adj_matrix, axis=1)
    for i in range(N):
        if out_degrees[i] == 0:
            adj_matrix[i, :] = 1.0 / N
        else:
            adj_matrix[i, :] /= out_degrees[i]

    # Iterimi i PageRank
    pr = np.ones(N) / N
    for _ in range(num_iter):
        pr = (1 - d) / N + d * np.dot(adj_matrix.T, pr)
        
    return {articles[i]['id']: pr[i] for i in range(N)}
