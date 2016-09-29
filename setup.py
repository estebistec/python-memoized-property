#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(
    name='memoized-property',
    version='1.0.3',
    description='A simple python decorator for defining properties that only run their fget function once',
    long_description=readme + '\n\n' + history,
    author='Steven Cummings',
    author_email='cummingscs@gmail.com',
    url='https://github.com/estebistec/python-memoized-property',
    py_modules=['memoized_property'],
    license="BSD",
    zip_safe=False,
    keywords='memoized property decorator',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)
