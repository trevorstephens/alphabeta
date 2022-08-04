#! /usr/bin/env python

"""alphabeta - A/B testing tools."""

from setuptools import setup, find_packages
import alphabeta

DESCRIPTION = __doc__
VERSION = alphabeta.__version__

setup(name='alphabeta',
      version=VERSION,
      description=DESCRIPTION,
      long_description=open("README.rst").read(),
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Topic :: Software Development',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Programming Language :: Python :: 3.10'],
      author='Trevor Stephens',
      author_email='trev.stephens@gmail.com',
      url='https://github.com/trevorstephens/alphabeta',
      license='new BSD',
      packages=find_packages(exclude=['*.tests',
                                      '*.tests.*']),
      zip_safe=False,
      package_data={'': ['LICENSE']},
      install_requires=['scipy'])
