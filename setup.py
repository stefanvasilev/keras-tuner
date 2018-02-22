"""Setup script."""
from setuptools import find_packages
from setuptools import setup

setup(
    name="Kerastuner",
    version="0.1",
    description="Hypertuner for Keras",
    install_requires=open("requirements.txt").read().splitlines(),
    packages=find_packages(),
)