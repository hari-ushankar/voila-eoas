#!/usr/bin/env python

# Setup script for PyPI; use CMakeFile.txt to build extension modules

from setuptools import setup


setup(
    name='rad_lib',
    packages=['rad_lib'],
    classifiers=[
        'License :: OSI Approved :: BSD License'
    ],
    long_description="""python tools for libradtran""")
