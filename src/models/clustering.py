from random import sample

import hdbscan
from sentence_transformers import SentenceTransformer

from src.models.preprocessor import Preprocessor


class Cluster:

    def __init__(self, model):
        self.df = None
        self.prepr = Preprocessor()
        self.model = SentenceTransformer(model)
        self.X = None
        self.tags = []

    def clear_tags(self):
        self.tags = []

    def vectorize(self):
        self.X = self.model.encode(self.df.X.tolist())

    def clustering(self, _min):
        dbscan = hdbscan.HDBSCAN(min_cluster_size=_min,
                                 min_samples=_min,
                                 allow_single_cluster=True,
                                 )
        clustering = dbscan.fit(self.X)
        self.df['cluster'] = clustering.labels_

    def get_result(self):
        _df = self.df['cluster'].value_counts(ascending=False)
        for index, count in zip(_df.index, _df):
            if index != -1:
                if len(self.df.loc[self.df.cluster == index, 'X'].unique().tolist()) > 3:
                    self.tags.append({'cluster': index,
                                      'text': '___'.join(sample(self.df.loc[self.df.cluster == index,
                                                                            'X'].unique().tolist(), 3)),
                                      'count': count})
                else:
                    self.tags.append({'cluster': index,
                                      'text': '___'.join(self.df.loc[self.df.cluster == index, 'X'].unique().tolist()),
                                      'count': count})

    def apply(self, df, _min, _translate):
        self.df = self.prepr.apply(df, _translate)
        self.vectorize()
        self.clustering(_min)
        self.get_result()
        return self.tags
