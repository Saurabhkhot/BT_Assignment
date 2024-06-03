import logging

logging.basicConfig(
    filename= 'Logs\\operations_log.log',
    level = logging.INFO,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('RestAPI_Logger')
