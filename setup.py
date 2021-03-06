#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pandas>=0.20',
]

setup_requirements = [
    'pytest-runner',
    # TODO(jfishe): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    'pylint',
    'mypy',
    # TODO: put package test requirements here
]

setup(
    name='paperless',
    version='0.1.1',
    description="Convert Paperless XML format to CSV for import to Todoist",
    long_description=readme + '\n\n' + history,
    author="John D. Fisher",
    author_email='jdfenw@gmail.com',
    url='https://github.com/jfishe/paperless',
    packages=find_packages(include=['paperless']),
    entry_points={
        'console_scripts': [
            'paperless=paperless.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='paperless',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
