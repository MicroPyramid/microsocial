#!/usr/bin/env python
from setuptools import setup

setup(
      name='microsocial',
      version='0.0.1',
      #install_requires=['lxml', 'PIL'],
      description='microsocial is collection of social apis for python. It supports authentication, posting, sharing etc.',
      author='MicroPyramid',
      author_email='MicroPyramid@googlegroups.com',
      maintainer='Ashwin',
      maintainer_email='MicroPyramid@googlegroups.com',
      url='http://github.com/micropyramid/microsocial',

      license='GPL3',
      long_description=open('README.rst').read(),

      keywords = 'Google+ API, Facebook API, Twitter API, Linkedin API, GitHub API, Social API for python',
      packages=['microsocial'],
      include_package_data=True,
      zip_safe=True,
      )
