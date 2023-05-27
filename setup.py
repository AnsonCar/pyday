import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyday_AnsonCar",
    version="0.0.1",
    author="AnsonCar",
    author_email="anson1tsang@gmail.com",
    description = "This Python package aims to provide fast and convenient methods for processing, analyzing, and visualizing data. It will offer a range of features and tools to assist users in data preprocessing, statistical analysis, and visualization, enabling them to better understand and accurately present their data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnsonCar/pyday",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
