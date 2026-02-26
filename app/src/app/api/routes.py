"""API route handlers."""

from typing import Any, Dict

from app.main import create_app


def get_status() -> Dict[str, Any]:
    """Handle GET /status - return application status."""
    app = create_app()
    return app.get_status()


def trigger_deploy(environment: str, version: str) -> Dict[str, Any]:
    """Handle POST /deploy - trigger deployment."""
    app = create_app()
    return app.deploy(environment, version)
