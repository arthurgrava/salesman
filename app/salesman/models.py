#encoding:utf-8


DEFAULT_SOURCE_ID = u'user_id'
DEFAULT_TARGET_ID = u'item_id'
DEFAULT_LIMIT = 16

class RecommendationModel(object):
    def __init__(self, observed_data, recommendations, source_id=DEFAULT_SOURCE_ID, target_id=DEFAULT_TARGET_ID):
        self.observed_data = observed_data
        self.recommendations = recommendations
        self.source_id = source_id
        self.target_id = target_id


    def get_recommendations(self, source_id, limit=DEFAULT_LIMIT):
        """
        Returns recommendations for the specified user
        """
        return self.recommendations[user_id]