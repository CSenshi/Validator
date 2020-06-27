# python setup.py bdist_wheel

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


__major__ = 0
__minor__ = 1
__patch__ = 5
__version__ = ".".join([str(__major__), str(__minor__), str(__patch__)])

setup(
    name="validator",
    version=__version__,
    description=("Python Validator"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["validator", "validator.rules_src", "validator.parser"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={"dev": ["pytest", "black"]},
    url="https://github.com/CSenshi/Validator",
    author="Saba Pockhua",
    author_email="saba.pochkhua@gmail.com",
)
