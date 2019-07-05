#!/bin/env python
import os

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Pull version from source without importing
# since we can't import something we haven't built yet :)
exec(open(os.path.join(here, 'iexdata', 'version.py')).read())

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'requests>=2.21.0',
    'socketIO-client-nexus>=0.7.6',
    'ujson>=1.35',
    'retry>=0.9.2'
]

setup(
    name='iex-data',
    version=__version__,
    python_requires='>=3.7.*',
    description='API Client library for IEX market data',
    url='https://github.com/aolsux/iex-data',
    download_url='https://pypi.org/project/iex-data',
    author='Martin Rückl',
    author_email='rueckl@xelonic.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='finance data api client stream rest http',
    zip_safe=False,
    packages=find_packages(exclude=("test", "test.*")),
    install_requires=requires,
    extras_require={'dev': requires + ['unittest']}
)
