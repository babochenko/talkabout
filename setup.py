"""
Setup configuration for the pyllm package.
"""

from setuptools import setup, find_packages

setup(
    name="talkabout",
    version="0.1.0",
    author="Denis Babochenko",
    author_email="babochenko.denis2@gmail.com",
    description="AI-powered object query proxy using OpenAI",
    long_description="TalkAbout allows you to query any Python object using natural language. Simply wrap your object in a Proxy and ask questions about it in plain English. The AI will generate the appropriate Python code to access or compute the requested information.",
    long_description_content_type="text/plain",
    url="https://github.com/yourusername/talkabout",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.900",
        ],
        "finance": [
            "yfinance>=0.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "talkabout=talkabout.main:main",
        ],
    },
)