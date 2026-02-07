from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_similarity(emb1, emb2):
    emb1 = np.array(emb1).reshape(1, -1)
    emb2 = np.array(emb2).reshape(1, -1)
    return cosine_similarity(emb1, emb2)[0][0]
