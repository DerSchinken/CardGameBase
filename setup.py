from setuptools import setup, find_packages

# Get long description
with open("README.md", "r") as readme:
    long_description = readme.read()

# Get requirements
with open("requirements.txt", "r") as reqs:
    requirements = reqs.read().splitlines()

setup(
    name="CardGameBase",
    version="1.0.4",
    # Major version 1
    # Minor version 0
    # Maintenance version 0

    author="DerSchinken",
    maintainer="DerSchinken",
    description="Card Game Base with basic deck and card class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">= 3.7",
    url="https://github.com/DerSchinken/CardGameBase/",
    keyword=[
        "Card Game",
        "Game",
        "Cards"
    ],
    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ]
)
