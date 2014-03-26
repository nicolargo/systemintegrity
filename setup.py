#!/usr/bin/env python

# import os
# import sys
# import glob

from setuptools import setup

data_files = [
    ('share/doc/systemintegrity', ['AUTHORS', 'README.md'])
]

setup(
    name='systemintegrity',
    version='0.1',
    description="...",
    long_description=open('README.md').read(),
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/systemintegrity',
    #download_url='https://s3.amazonaws.com/systemintegrity/systemintegrity-1.2.tar.gz',
    license="MIT",
    keywords="system, integrity, sha, sha-2",
    packages=['systemintegrity'],
    include_package_data=True,
    data_files=data_files,
    # test_suite="witsub.test",
    entry_points={"console_scripts": ["systemintegrity=systemintegrity.systemintegrity:main"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT licence',
        'Programming Language :: Python :: 2',
    ]
)
