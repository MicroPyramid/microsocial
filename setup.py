#!/usr/bin/env python
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
      name='microsocial',
      version='0.0.1',
      install_requires=['requests==2.0.0', 'requests_oauthlib==0.3.2'],
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
      classifiers=[
        'Development Status :: 0 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet'
    ]
)
