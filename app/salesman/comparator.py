# encoding:utf-8
import math


class Pearson(object):
    """
    Person correlation comparator class
    """
    def compare(self, data, id1, id2, user_label, item_label, score_label, user_means):
        """
        Returns the pearson correlation value of user 1 (id1) ans user 2 (id2)
        ans concerning that Ia = [...], Ib = [...] and Iab = Ia INTERSECTION Ib
        """
        self._lbl_item = item_label
        self._lbl_user = user_label
        self._lbl_score = score_label

        data_id1 = data[data[user_label] == id1]
        data_id2 = data[data[user_label] == id2]
        
        rated_id1 = set(data_id1[item_label])
        rated_id2 = set(data_id2[item_label])
        both_rated = rated_id1.intersection(rated_id2)

        up, d1, d2 = 0.0, 0.0, 0.0
        for item_id in both_rated:
            r1 = sum(data_id1[data[item_label] == item_id][score_label])
            r2 = sum(data_id2[data[item_label] == item_id][score_label])
            up += ((r1 - user_means[id1]) * (r2 - user_means[id2]))
            d1 += ((r1 - user_means[id1]) ** 2)
            d2 += ((r2 - user_means[id2]) ** 2)

        # preventing division by 0
        if d1 == 0.0:
            d1 = 1.0
        if d2 == 0.0:
            d2 = 1.0

        return up / math.sqrt(d1 * d2)


pearson = Pearson()