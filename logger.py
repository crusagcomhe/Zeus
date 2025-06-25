# zeus/logger.py

import logging

def get_logger(name="zeus"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler()],
    )
    return logging.getLogger(name)
