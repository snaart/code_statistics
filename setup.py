from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="code-statistics",
    version="0.1.0",
    author="NikitaStepanov",
    author_email="stepanov.iop@gmail.com",
    description="Инструмент для подсчета статистики кода в проектах",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snaart/code-statistics",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "code-stats=code_statistics.cli:cli_main",
        ],
    },
) 