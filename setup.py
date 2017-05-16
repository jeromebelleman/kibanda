#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='kibanda',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Manage Kibana dashboards",
    long_description="List, edit, back up Kibana dashboards.",
    scripts=['kibanda'],
    data_files=[('share/man/man1', ['kibanda.1'])],
)
