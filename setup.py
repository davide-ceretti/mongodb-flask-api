#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'flask==0.10.1',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mongodb-flask-api',
    version='0.1.0',
    description="A simple API built on top of MongoDB and Flask",
    long_description=readme + '\n\n' + history,
    author="Davide Ceretti",
    author_email='dav.ceretti@gmail.com',
    url='https://github.com/davide-ceretti/mongodb-flask-api',
    packages=[
        'api',
    ],
    package_dir={'api':
                 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='mongodb-flask-api',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
