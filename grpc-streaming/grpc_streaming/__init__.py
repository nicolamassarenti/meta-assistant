__version__ = "0.1.0"

from loguru import logger

import functools
import traceback


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"Function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"Function {func.__name__} returned result {result}")
            return result
        except Exception as e:
            logger.exception(
                f"Exception raised in {func.__name__}. Exception: {str(e)}, Traceback: {traceback.format_exc()}"
            )
            raise e

    return wrapper
