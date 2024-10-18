"""Setup script for the ral_color_converter package."""

from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="ral_color_converter",
    version="1.0.0",
    description="A tool to convert images from RGB to RAL Classic color space.",
    author="Johannes Voigt",
    url="https://github.com/JohannesVoigt/ral-color-converter",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ral_color_converter=run_color_converter:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
