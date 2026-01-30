"""Setup script for csvjson."""

from setuptools import setup, find_packages

setup(
    name="csvjson",
    version="1.0.0",
    description="A CLI tool to convert CSV files to JSON",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0"],
    },
    entry_points={
        "console_scripts": [
            "csvjson=csvjson.cli:main",
        ],
    },
)
