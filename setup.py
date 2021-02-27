import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fattails", # Replace with your own username
    version="0.0.3",
    author="FergM",
    description="A package for fat-tailed statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FergM/fattails/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas>=1.2.0',
        'matplotlib>=3.3.3'
    ],
    python_requires='>=3.7',
)
