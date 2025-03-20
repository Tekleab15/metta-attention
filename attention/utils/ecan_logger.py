import logging
import os

def setup_logger(log_level= logging.DEBUG, log_file = "ecan_debug.log"):

    logger = logging.getLogger("ECANLogger")
    logger.setLevel(log_level)
    
    # Clear any existing handlers to avoid duplicate logging when re-imported.
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # File handler for persistent logging (captures DEBUG and above).
    fh = logging.FileHandler(log_file)
    fh.setLevel(log_level)

    # Stream handler for console output (captures INFO and above).
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Define a formatter with time, logger name, log level, and message.
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add both handlers to the logger.
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info("Logger initialized at level %s; log file: %s", logging.getLevelName(log_level), os.path.abspath(log_file))
    return logger


if __name__ == '__main__':

    # Simple test block to demonstrate the logger output.
    logger = setup_logger()
    logger.debug("This is a DEBUG message (for tracing detailed steps).")
    logger.info("This is an INFO message (general information).")
    logger.warning("This is a WARNING message (something to be cautious about).")
    logger.error("This is an ERROR message (an error occurred).")
    logger.critical("This is a CRITICAL message (a severe error occurred).")
