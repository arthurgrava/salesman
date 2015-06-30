#encoding:utf-8
import pandas as pd
from models import RecommendationModel
from comparator import pearson

DEFAULT_SOURCE_ID = u'user_id'
DEFAULT_TARGET_ID = u'item_id'
DEFAULT_SCORE_COL = u'score'


class UserBased(object):
    def __init__(self):
        self.data = None
        self.items = None
        self.users = None


    def calculate(self, data, source_id=DEFAULT_SOURCE_ID, target_id=DEFAULT_TARGET_ID, score=DEFAULT_SCORE_COL):
        """
        Calculates a recommendation model
        """
        if source_id not in data or target_id not in data or score not in data:
            raise ValueError(u'Some of the columns were not found at the data source')

        self.data = data

        self.items = set(data[target_id])
        self.users = set(data[source_id])
        recommendations = pd.DataFrame()

        for user in self.users:
            similar_users = self._retrieve_similar_users(user)
            not_rated_items = self._retrieve_not_rated_items(data[data[source_id] == user])
            for item in not_rated_items:
                predicted = self._predict(user, similar_users, item)
                if predicted > 0:
                    recommendations = recommendations.append(pd.DataFrame(
                        [[user, item, predicted]],
                        columns=[source_id, item_id, u'predicted'],
                    ), ignore_index=True)
        recommendations = recommendations.sort(columns=['user_id', 'score'], ascending=False)

        return RecommendationModel(observed_data=data, recommendations=recommendations, source_id=source_id, target_id=target_id)

    def _retrieve_similar_users(self, source_id):
        """
        Calculates the similarity of each user on the data source
        """
        similarity = pd.DataFrame()
        for candidate in self.users:
            if candidate != source_id:
                similarity = similarity.append(pd.DataFrame(
                    [[source_id, candidate, pearson.compare(self.data, source_id, candidate)]],
                    columns=['user_id', 'similar_id', 'score']
                ), ignore_index=True)

        return similarity.sort(columns=['user_id', 'score'], ascending=False)

















