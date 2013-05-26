#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-hash-password',
    version='0.0.1',
    description='Generate hashed passwords.',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/django-hash-password',
    requires=['Django (>=1.3.0)'],
    packages=find_packages(),
    license='MIT License',
    zip_safe=True)