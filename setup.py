# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='django_url_decorator',
    version='1.0.0',
    description='Django url decorator',
    author='sammyrulez',
    url='https://github.com/sammyrulez/django_url_decorator',
    license='BSD',
    packages = ['django_url_decorator'],
    long_description=open('README.md').read(),
    install_requires=['Django>=1.4']
)