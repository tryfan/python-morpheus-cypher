#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='morpheus-cypher',
    version='0.1.3',
    description='Retrieve secrets from Morpheus Cypher Secret Storage',
    author='Nick Celebic',
    author_email='ncelebic@morpheusdata.com',
    url='https://github.com/tryfan/python-morpheus-cypher',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.21.0'
    ]
)
