# encoding:utf-8
import logging


# app name
APP = u'salesman'

# logging configuration
LOGGING = {
    APP: {
        'level': logging.INFO,
        'log_format': u'%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)d\t%(message)s',
        'file_path': u'/var/log/salesman/output.log',
    }
}

# default properties
DEFAULT_USER_LABEL = u'user_id'
DEFAULT_ITEM_LABEL = u'item_id'
DEFAULT_SCORE_label_LABEL = u'score'
DEFAULT_LIMIT = 16
