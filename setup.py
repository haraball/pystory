# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Doc

TODO: make script to put in bin so that it runs and stuff.

('Pystory is a virtual environment sensitive logger. ',
                 'Logs all the commands you run while in an active virtual environment.'),
"""

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pystory',
    version='0.2',
    description='A virtual environment utility for saving the commands you use in python projects.',
    long_description=readme,
    author='Harald Kirkerød',
    author_email='haraball+pystory@gmail.com',
    url='https://github.com/haraball/pystory',
    license=license,
    entry_points={
        'console_scripts': ['pystory = pystory.__main__:main']},
    packages=find_packages(exclude=('tests', 'docs')),
)
