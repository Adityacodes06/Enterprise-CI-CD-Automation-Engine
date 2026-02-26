"""Unit tests for API routes."""

from unittest.mock import MagicMock, patch

import pytest

from app.api.routes import get_status, trigger_deploy


class TestGetStatus:
    """Tests for get_status route."""

    def test_get_status_returns_dict(self):
        """get_status returns dict with status info."""
        result = get_status()

        assert isinstance(result, dict)
        assert "status" in result
        assert "version" in result
        assert "health" in result

    def test_get_status_health_structure(self):
        """get_status includes nested health check."""
        result = get_status()

        assert "ready" in result["health"]
        assert "alive" in result["health"]


class TestTriggerDeploy:
    """Tests for trigger_deploy route."""

    def test_trigger_deploy_blue(self):
        """trigger_deploy for blue returns success."""
        result = trigger_deploy("blue", "1.0.0")

        assert result["success"] is True
        assert result["environment"] == "blue"
        assert result["version"] == "1.0.0"

    def test_trigger_deploy_green(self):
        """trigger_deploy for green returns success."""
        result = trigger_deploy("green", "2.0.0")

        assert result["success"] is True
        assert result["environment"] == "green"
