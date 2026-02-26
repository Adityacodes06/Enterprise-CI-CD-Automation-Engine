"""Health check service for application monitoring."""

import time
from typing import Dict


class HealthChecker:
    """Service for health and readiness checks."""

    def __init__(self):
        """Initialize health checker."""
        self._start_time = time.time()

    def check(self) -> Dict[str, bool]:
        """Perform health check and return status."""
        return {
            "ready": self.is_healthy(),
            "alive": True,
        }

    def is_healthy(self) -> bool:
        """Return whether the application is healthy."""
        # Simple check - can be extended with DB, cache, etc.
        return True

    def get_uptime_seconds(self) -> float:
        """Return application uptime in seconds."""
        return time.time() - self._start_time
