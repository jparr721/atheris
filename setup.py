import os
from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="atheris",
    version="1.0.0",
    author="Jarred Parr",
    author_email="jparr721@gmail.com",
    install_requires=[],
    scripts=["bin/atheris"],
    description="Stop being a pirce of shit",
    license="MIT",
    long_description=read("README.md"),
)
