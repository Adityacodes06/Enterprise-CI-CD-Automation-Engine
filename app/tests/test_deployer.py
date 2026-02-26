"""Unit tests for DeploymentService."""

import pytest

from app.services.deployer import DeploymentService


class TestDeploymentService:
    """Tests for DeploymentService."""

    def test_init_default_env(self):
        """Service initializes with blue as default."""
        service = DeploymentService({})
        assert service.active_env == "blue"

    def test_init_custom_default_env(self):
        """Service uses config default_env when provided."""
        service = DeploymentService({"default_env": "green"})
        assert service.active_env == "green"

    def test_deploy_to_blue(self):
        """Deploy to blue environment succeeds."""
        service = DeploymentService({})
        result = service.deploy("blue", "1.0.0")

        assert result["success"] is True
        assert result["environment"] == "blue"
        assert result["version"] == "1.0.0"
        assert service.get_active_environment() == "blue"

    def test_deploy_to_green(self):
        """Deploy to green environment succeeds."""
        service = DeploymentService({"default_env": "blue"})
        result = service.deploy("green", "2.0.0")

        assert result["success"] is True
        assert result["environment"] == "green"
        assert result["previous_env"] == "blue"

    def test_deploy_invalid_environment_raises(self):
        """Deploy to invalid environment raises ValueError."""
        service = DeploymentService({})

        with pytest.raises(ValueError, match="Invalid environment"):
            service.deploy("red", "1.0.0")

    def test_get_active_environment(self):
        """get_active_environment returns current env."""
        service = DeploymentService({})
        assert service.get_active_environment() == "blue"

        service.deploy("green", "1.0.0")
        assert service.get_active_environment() == "green"

    def test_rollback(self):
        """Rollback switches to target environment."""
        service = DeploymentService({"default_env": "blue"})
        service.deploy("green", "2.0.0")

        result = service.rollback("blue")

        assert result["success"] is True
        assert result["environment"] == "blue"
        assert result["version"] == "rollback"
        assert service.get_active_environment() == "blue"
