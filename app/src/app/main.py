"""Main application module for the CI/CD Automation Engine."""

import json
import logging
from datetime import datetime
from typing import Any, Dict, Optional

from app.services.deployer import DeploymentService
from app.services.health import HealthChecker

logger = logging.getLogger(__name__)


class Application:
    """Main application orchestrator."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize application with optional config."""
        self.config = config or {}
        self.deployer = DeploymentService(self.config.get("deploy", {}))
        self.health_checker = HealthChecker()

    def run(self) -> bool:
        """Run the application main loop."""
        logger.info("Starting application")
        return self.health_checker.is_healthy()

    def get_status(self) -> Dict[str, Any]:
        """Return application status."""
        return {
            "status": "running",
            "version": "1.0.0",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "health": self.health_checker.check(),
        }

    def deploy(self, environment: str, version: str) -> Dict[str, Any]:
        """Trigger deployment to specified environment."""
        return self.deployer.deploy(environment, version)


def create_app(config: Optional[Dict[str, Any]] = None) -> Application:
    """Factory function to create application instance."""
    return Application(config)
