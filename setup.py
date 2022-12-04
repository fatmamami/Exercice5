from distutils.core import setup
from setuptools import find_packages

setup(

    name="snowflake",
    version="1",
    author="DSSS",
    author_email="fatma.mami@fau.de",
    packages=find_packages(),
    install_requires=["numpy","turtles"]
)