"""Structured logging configuration for C64-KB-Agent."""

import logging
import sys
from typing import Any

try:
    import structlog

    HAS_STRUCTLOG = True
except ImportError:
    HAS_STRUCTLOG = False


def setup_logging(log_level: str = "INFO") -> Any:
    """Configures structured logging or standard logging."""
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    if HAS_STRUCTLOG:
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.StackInfoRenderer(),
                structlog.dev.set_exc_info,
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.dev.ConsoleRenderer(),
            ],
            wrapper_class=structlog.make_filtering_bound_logger(numeric_level),
            context_class=dict,
            logger_factory=structlog.PrintLoggerFactory(),
            cache_logger_on_first_use=True,
        )
        return structlog.get_logger()
    else:
        logging.basicConfig(
            level=numeric_level,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            handlers=[logging.StreamHandler(sys.stdout)],
        )
        return logging.getLogger("c64_kb_agent")


logger = setup_logging()
