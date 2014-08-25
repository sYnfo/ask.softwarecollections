#!/usr/bin/env python

from setuptools import setup

setup(
    name='ask.softwarecollections',
    version='1.0',
    description='Askbot for ask.softwarecollections.org',
    author='Matej Stuchlik',
    author_email='mstuchli@redhat.com',
    url='https://github.com/mstuchli/ask.softwarecollections',
    license='GPLv3+',
    install_requires=[
        'Django==1.5',
        'psycopg2',
        'askbot',
        'django-rosetta',
        'django-redis-cache',
        'hiredis',
    ]
)
