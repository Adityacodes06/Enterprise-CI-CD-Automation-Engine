"""Deployment service for managing blue-green deployments."""

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class DeploymentService:
    """Service for orchestrating deployments."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize with deployment configuration."""
        self.config = config
        self.active_env: str = config.get("default_env", "blue")

    def deploy(self, environment: str, version: str) -> Dict[str, Any]:
        """Execute deployment to specified environment."""
        logger.info("Deploying version %s to %s", version, environment)

        if environment not in ("blue", "green"):
            raise ValueError(f"Invalid environment: {environment}")

        result = {
            "success": True,
            "environment": environment,
            "version": version,
            "previous_env": self.active_env,
        }

        self.active_env = environment
        return result

    def get_active_environment(self) -> str:
        """Return currently active deployment environment."""
        return self.active_env

    def rollback(self, target_env: str) -> Dict[str, Any]:
        """Rollback to specified environment."""
        logger.info("Rolling back to %s", target_env)
        return self.deploy(target_env, "rollback")
