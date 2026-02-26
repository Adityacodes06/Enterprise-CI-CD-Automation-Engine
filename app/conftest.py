"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_config():
    """Sample deployment configuration."""
    return {
        "deploy": {"default_env": "blue"},
        "health": {"timeout": 30},
    }
