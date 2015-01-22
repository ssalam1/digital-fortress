#!/usr/bin/env python

from setuptools import setup

execfile('fandjango/version.py')

readme = open('README.rst').read()
history = open('HISTORY.rst').read()

setup(
    name = 'fandjango',
    version = __version__,
    description = "Fandjango makes it stupidly easy to create Facebook applications with Django.",
    long_description = readme + '\n\n' + history,
    author = "Johannes Gorset",
    author_email = "jgorset@gmail.com",
    url = "http://github.com/jgorset/fandjango",
    packages = [
        'fandjango',
        'fandjango.migrations',
        'fandjango.templatetags'
    ],
    package_data = {
        'fandjango': [
            'templates/fandjango/*',
            'locale/no_NB/LC_MESSAGES/*'
        ]
    },
    install_requires = [
        'facepy >= 0.8',
        'requests >= 0.8'
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
