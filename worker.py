import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

while True:
    logger.info("Worker is running...")
    time.sleep(5)
