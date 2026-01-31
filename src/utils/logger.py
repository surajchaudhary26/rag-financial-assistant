import logging
import sys
from pathlib import Path


def setup_logger(name: str = "rag_app", log_level=logging.INFO):
    """
    Creates and returns a configured logger.
    """

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers if re-imported
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(log_dir / "app.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
