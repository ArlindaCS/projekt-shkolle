import math

def tokenize(text):
    """Kthen tekstin në shkronja të vogla dhe e ndan në fjalë."""
    return text.lower().replace('.', '').replace(',', '').split()

def calculate_tf(term, tokenized_text):
    """Llogarit Term Frequency (sa herë shfaqet fjala)."""
    if not tokenized_text:
        return 0
    return tokenized_text.count(term.lower()) / len(tokenized_text)

def compute_relevance(query, article):
    """Llogarit pikët e thjeshtuara të relevancës bazuar te titulli dhe abstrakti."""
    query_terms = tokenize(query)
    title_tokens = tokenize(article['title'])
    abstract_tokens = tokenize(article['abstract'])
    
    score = 0.0
    for term in query_terms:
        # Jepet më shumë peshë nëse fjala ndodhet te titulli
        score += calculate_tf(term, title_tokens) * 2.0
        score += calculate_tf(term, abstract_tokens) * 1.0
    return score
