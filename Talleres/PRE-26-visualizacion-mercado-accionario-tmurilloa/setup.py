"""Package installer"""

from setuptools import find_packages, setup  # type: ignore

setup(
    name="homework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ipykernel",
        "matplotlib",
        "pandas",
        "numpy",
        "pytest",
        "scikit-learn",
    ],
)
