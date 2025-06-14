from .Singleton import Singleton
import logging
import logging.config

class Logger(metaclass=Singleton):
    logger = None
    def __call__(self, TIMESTAMP):
        #super.__new__()
        logging.config.fileConfig("resources/log_settings.conf", 
                          defaults={ 'logfilename': 'results/' + TIMESTAMP + '/pytest.txt' })
        logger = logging.getLogger(__name__)
        logger.propagate=True
    
    def info(message):
        logging.info(message)

    def debug(message):
        logging.debug(message)

    def warn(message):
        logging.warning(message)
