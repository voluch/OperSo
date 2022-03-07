from src.models.clustering import Cluster

def test():
    import pandas as pd
    df = pd.read_csv("src/data/test.csv", header=None, nrows=20)
    clust = Cluster()
    clust.fit(df)
    # print(clust.X)

test()


# def model_test():
#     from sentence_transformers import SentenceTransformer
#     from sklearn.metrics.pairwise import cosine_similarity
#     import numpy as np
#     model = SentenceTransformer('all-mpnet-base-v2')
#     # print(np.transpose(model.encode('коронавірус').reshape(-1, 1)).shape)
#     print(cosine_similarity(np.transpose(model.encode('коронавірус').reshape(-1, 1)), np.transpose(model.encode('коронавирус').reshape(-1, 1))))
#
# model_test()