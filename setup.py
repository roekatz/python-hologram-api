#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from __future__ import absolute_import
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
]

setup_requirements = [
]

test_requirements = [
    'flake8'
]

setup(
    name='python_hologram_api',
    version='0.1.6',
    description="Python client for https://dashboard.hologram.io/api.",
    long_description=readme + '\n\n' + history,
    author="Victor Yap",
    author_email='victor@vicyap.com',
    url='https://github.com/vicyap/python-hologram-api',
    packages=find_packages(include=['python_hologram_api']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_hologram_api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
