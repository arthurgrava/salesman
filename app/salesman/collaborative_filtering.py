#encoding:utf-8
import logging
import pandas as pd
from comparator import pearson
from conf import *
from models import RecommendationModel


logger = logging.getLogger(APP)


class UserBased(object):
    """
    User based collaborative filtering implementation
    """
    def __init__(self):
        self.data = None
        self.items = None
        self.users = None
        self.item_label = None
        self.user_label = None
        self.score_label = None
        self.means = None


    def _validate_input(self, data, user_label, item_label, score_label):
        """
        Valides if the expected columns are present on the dataset
        """
        if type(data) is pd.DataFrame:
            columns_name = data.columns
        else:
            columns_name = data.column_names()
        if user_label not in columns_name or item_label not in columns_name or score_label not in columns_name:
                logger.error(u'Invalid input, a ValueError will be raised')
                raise ValueError(u'Some of the columns were not found at the data source')


    def calculate(self, data, user_label=DEFAULT_USER_LABEL, item_label=DEFAULT_ITEM_LABEL, score_label=DEFAULT_SCORE_label_LABEL):
        """
        Calculates a recommendation model
        """
        self._validate_input(data, user_label, item_label, score_label)

        logger.info(u'Initiating UserBased collaborative filtering calculation')

        # defining class attributes
        self.data = data
        self.items = set(data[item_label])
        self.users = set(data[user_label])
        self.item_label = item_label
        self.user_label = user_label
        self.score_label = score_label
        self.means = {}
        recommendations = pd.DataFrame()

        total_users = len(self.users)

        logger.info(u'Starting to calculate the mean rate of each user, the total number of users is -- {0}'.format(total_users))
        # calculates the mean score for every user
        for user_id in self.users:
            detail_data = data[data[user_label] == user_id][score_label]
            sample_mean = len(detail_data)
            if sample_mean:
                self.means[user_id] = sum(detail_data) / len(detail_data)
            else:
                self.means[user_id] = 0.0
            logger.info(u'Mean rate calculated for user -- {0}, value is -- {1}'.format(user_id, self.means[user_id]))

        for user_id in self.users:
            logger.info(u'Predicting entries for user -- {0}, total users is -- {1}'.format(user_id, total_users))
            similar_users = self._retrieve_similar_users(user_id)
            not_rated_items = self._retrieve_not_rated_items(user_id)
            user_data = data[data[user_label] == user_id]
            try:
                for item_id in not_rated_items:
                    predicted = self._predict(user_id, similar_users, item_id)
                    logger.debug(u'Predicted rate for user -- "{0}" on item -- "{1}"'.format(user_id, item_id))
                    if predicted > 0:
                        recommendations = recommendations.append(pd.DataFrame(
                            [[user_id, item_id, predicted]],
                            columns=[user_label, item_label, u'predicted'],
                        ), ignore_index=True)
            except Exception, e:
                logger.error(u'An error occurred when predicting the rating')
                logger.exception(e)
                return
        
        logger.info(u'All recommendations were calculated, a RecommendationModel will be instanciated')
        recommendations = recommendations.sort(columns=[user_label, 'predicted'], ascending=False)

        return RecommendationModel(observed_data=data, recommendations=recommendations, user_label=user_label, item_label=item_label)

    def _retrieve_similar_users(self, user_id, k=10):
        """
        Calculates the similarity of each user on the data source
        """
        similarity = pd.DataFrame()
        for candidate in self.users:
            if candidate != user_id:
                similarity = similarity.append(
                    pd.DataFrame(
                        [[user_id, candidate, pearson.compare(self.data, user_id, candidate, self.user_label, self.item_label, self.score_label, self.means)]],
                        columns=['user_id', 'similar_id', 'score']
                    ), ignore_index=True
                )

        logger.info(u'Similar users gathered for user -- {0}'.format(user_id))
        return similarity.sort(columns=['user_id', 'score'], ascending=False)[:k]


    def _retrieve_not_rated_items(self, user_id):
        """
        Retrieve all items that the user did not rate
        """
        rated = set(self.data[self.data[self.user_label] == user_id][self.item_label])
        logger.info(u'Not rated items gathered for user -- {0}'.format(user_id))
        return list(self.items - rated)


    def _predict(self, user_id, similar_users, item_id):
        """
        Predict the rating for the user on the item, based on the rating of his
        similar users
        """
        sample = self.data[(self.data[self.user_label].isin(similar_users['similar_id'])) & (self.data[self.item_label] == item_id)]
        down_equation = sum(similar_users['score'])

        up_equation = self.means[user_id]
        for similar_id in similar_users['similar_id']:
            similarity = sum(similar_users[similar_users['similar_id'] == similar_id]['score'])
            mean_similar_rate = (sum(sample[sample[self.user_label] == similar_id][self.score_label]) - self.means[similar_id])
            up_equation += (similarity * mean_similar_rate)
        
        return up_equation / down_equation


class SocialFiltering(object):
    pass
