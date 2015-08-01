#encoding:utf-8
import logging
import conf


# setting up log configuration
logger = logging.getLogger(conf.APP)
logger.setLevel(logging.DEBUG)

default_formatter = logging.Formatter(conf.LOGGING[conf.APP]['log_format'])

file_handler = logging.handlers.WatchedFileHandler(conf.LOGGING[conf.APP]['file_path'])
file_handler.setLevel(conf.LOGGING[conf.APP]['level'])
file_handler.setFormatter(default_formatter)

logger.addHandler(file_handler)
logger.info(u'Log initiated: {0} to -> {1}'.format(conf.APP, conf.LOGGING[conf.APP]['file_path']))
