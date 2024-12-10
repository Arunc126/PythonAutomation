import inspect
import logging

import pytest as pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler=logging.FileHandler("..//utilities.log_file.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s", datefmt='%m/%d/%Y %H:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
