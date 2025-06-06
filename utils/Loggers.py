import logging
import os


def setup_logger(name: str, log_file: str = 'test_logs.log') -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    log_dir = 'C:/Py/Selenium/Capstone_Ecommerce/reports/logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, log_file)

    if logger.hasHandlers():
        logger.handlers.clear()

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
