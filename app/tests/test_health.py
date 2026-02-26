"""Unit tests for HealthChecker."""

import pytest

from app.services.health import HealthChecker


class TestHealthChecker:
    """Tests for HealthChecker."""

    def test_check_returns_expected_structure(self):
        """check returns dict with ready and alive keys."""
        checker = HealthChecker()
        result = checker.check()

        assert "ready" in result
        assert "alive" in result
        assert result["alive"] is True

    def test_is_healthy_returns_true(self):
        """is_healthy returns True for healthy state."""
        checker = HealthChecker()
        assert checker.is_healthy() is True

    def test_get_uptime_seconds(self):
        """get_uptime_seconds returns positive value."""
        checker = HealthChecker()
        import time
        time.sleep(0.01)  # Minimal sleep
        uptime = checker.get_uptime_seconds()
        assert uptime >= 0
