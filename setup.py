#!/usr/bin/env python

from setuptools import setup

setup(name='CloudIO',
      version='1.0',
      description='CloudIO is a Cloudstack Client written in Python',
      author='Gianni Carafa',
      author_email='gianni.carafa@srf.ch',
      url='https://github.com/mms-gianni/CloudIO',
      entry_points='''
        [console_scripts]
        cloudiosays=CloudIO.cloudiosays:main
        cloudiosays-inventory=CloudIO.cloudiosays:inventory
    ''',
      packages=['CloudIO'],
      )