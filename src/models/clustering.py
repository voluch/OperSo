from src.models.preprocessor import Preprocessor
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
import numpy as np

class Cluster:

    def __init__(self):
        self.df = None
        self.prepr = Preprocessor()
        self.X = None

    def vectorize(self):
        model = SentenceTransformer('all-mpnet-base-v2')
        self.X = model.encode(self.df.X.tolist())

    def clustering(self):
        dbscan = DBSCAN(eps=0.5, n_jobs=-1, metric="cosine")
        clustering = dbscan.fit(self.X)
        print(np.unique(clustering.labels_, return_counts=True))
        self.df['cluster'] = clustering.labels_
        print(self.df.loc[:, ['cluster', 'X']])

    def fit(self, df):
        self.df = self.prepr.fit(df)
        self.vectorize()
        self.clustering()


