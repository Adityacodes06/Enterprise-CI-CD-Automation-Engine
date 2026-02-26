"""Unit tests for main application module."""

from unittest.mock import MagicMock, patch

import pytest

from app.main import Application, create_app


class TestApplication:
    """Tests for Application class."""

    def test_init_default_config(self):
        """Application initializes with empty config when none provided."""
        app = Application()
        assert app.config == {}

    def test_init_with_config(self):
        """Application initializes with provided config."""
        config = {"deploy": {"default_env": "green"}}
        app = Application(config)
        assert app.config == config

    @patch("app.main.HealthChecker")
    def test_run_returns_healthy(self, mock_health_class):
        """Run returns True when health check passes."""
        mock_health = MagicMock()
        mock_health.is_healthy.return_value = True
        mock_health_class.return_value = mock_health

        app = Application()
        result = app.run()

        assert result is True
        mock_health.is_healthy.assert_called_once()

    @patch("app.main.HealthChecker")
    def test_run_returns_unhealthy(self, mock_health_class):
        """Run returns False when health check fails."""
        mock_health = MagicMock()
        mock_health.is_healthy.return_value = False
        mock_health_class.return_value = mock_health

        app = Application()
        result = app.run()

        assert result is False

    def test_get_status_structure(self):
        """get_status returns expected structure."""
        app = Application()
        status = app.get_status()

        assert "status" in status
        assert status["status"] == "running"
        assert "version" in status
        assert status["version"] == "1.0.0"
        assert "timestamp" in status
        assert "health" in status
        assert "ready" in status["health"]
        assert "alive" in status["health"]

    def test_deploy_calls_deployer(self):
        """deploy calls deployer and returns result."""
        app = Application()
        result = app.deploy("blue", "1.0.0")

        assert result["success"] is True
        assert result["environment"] == "blue"
        assert result["version"] == "1.0.0"


class TestCreateApp:
    """Tests for create_app factory."""

    def test_create_app_returns_application(self):
        """create_app returns Application instance."""
        app = create_app()
        assert isinstance(app, Application)

    def test_create_app_with_config(self):
        """create_app passes config to Application."""
        config = {"test": "value"}
        app = create_app(config)
        assert app.config == config
