from setuptools import setup, find_packages

setup(
    name="unscrambler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pypdf>=2.0.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        'console_scripts': [
            'unscrambler=unscrambler.cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for unscrambling PDF documents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/unscrambler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # Add system dependencies
    setup_requires=['setuptools'],
    install_requires=[
        "pypdf>=2.0.0",
        "pyyaml>=6.0",
    ],
    # Add system requirements
    system_requires=[
        "ghostscript",  # Required for PDF optimization
    ],
) 