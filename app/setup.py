"""Setup configuration for CI/CD Automation Engine."""

from setuptools import find_packages, setup

setup(
    name="cicd-automation-app",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
        ],
    },
)
