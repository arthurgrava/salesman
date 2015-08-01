#encoding:utf-8
import logging
from conf import *


logger = logging.getLogger(APP)


class RecommendationModel(object):
    """
    Basic recommendation model
    """
    def __init__(self, observed_data, recommendations, user_label=DEFAULT_USER_LABEL, item_label=DEFAULT_ITEM_LABEL):
        self.observed_data = observed_data
        self.recommendations = recommendations
        self.user_label = user_label
        self.item_label = item_label


    def get_recommendations(self, user_id, limit=DEFAULT_LIMIT):
        """
        Returns recommendations for the specified user
        """
        logger.info(u'Retrieving recommendations for user -- {0} with limit -- {1}'.format(user_id, limit))
        return self.recommendations[self.recommendations[self.user_label] == user_id]


    def to_csv(self, path):
        """
        Save recommendations as csv
        """
        self.recommendations.to_csv(path, sep=',', encoding='utf-8')


    def from_csv(self, path, *args, **kwargs):
        """
        Load recomendations from a csv file
        """
        pass
