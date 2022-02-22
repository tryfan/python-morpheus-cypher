#!/usr/bin/env python
import setuptools
import os


def get_version():
    version_filepath = os.path.join(os.path.dirname(__file__), "morpheuscypher", "version.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.strip().split()[-1][1:-1]


setuptools.setup(
    name='morpheus-cypher',
    version=get_version(),
    description='Retrieve secrets from Morpheus Cypher Secret Storage',
    author='Nick Celebic',
    author_email='ncelebic@morpheusdata.com',
    url='https://github.com/tryfan/python-morpheus-cypher',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.21.0'
    ]
)
