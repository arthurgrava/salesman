#encoding:utf-8


DEFAULT_SOURCE_ID = u'user_id'
DEFAULT_TARGET_ID = u'item_id'
DEFAULT_LIMIT = 16

class RecommendationModel(object):
    """
    Basic recommendation model
    """
    def __init__(self, observed_data, recommendations, user_label=DEFAULT_SOURCE_ID, item_label=DEFAULT_TARGET_ID):
        self.observed_data = observed_data
        self.recommendations = recommendations
        self.user_label = user_label
        self.item_label = item_label


    def get_recommendations(self, user_id, limit=DEFAULT_LIMIT):
        """
        Returns recommendations for the specified user
        """
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
