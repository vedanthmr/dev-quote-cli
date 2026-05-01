from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dev-quote-cli",
    version="1.0.0",
    author="Vedanth M",
    author_email="vedanthmofficial@gmail.com",
    description="A CLI tool to fetch daily programming quotes and dev jokes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vedanthmr/dev-quote-cli",
    py_modules=["quote_cli"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "quote=quote_cli:main",
        ],
    },
)