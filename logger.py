import os
import logging
from functools import wraps
from logging.handlers import RotatingFileHandler

# Create a custom logger
logger = logging.getLogger('my_app_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler for the log file
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'app.log')

file_handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def log_args_and_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f'Function {func.__name__} called with args: {args}, kwargs: {kwargs}')
            result = func(*args, **kwargs)
            logger.info(f'Function {func.__name__} returned: {result}')
            return result
        except Exception as e:
            logger.error(f'Function {func.__name__} raised an exception: {str(e)}')
            raise e
    return wrapper
