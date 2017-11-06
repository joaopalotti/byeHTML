from distutils.core import setup

from setuptools import find_packages, setup
from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop


requirements = [
    "justext >= 2.2.0",
    "beautifulsoup4 >= 4.5.0",
    "chardet >= 2.3.0"
]

setup(name='byeHTML',
        version='0.0.2',
        author='Joao Palotti',
        author_email='joaopalotti@gmail.com',
        license='LICENSE.txt',
        install_requires=requirements,
        url='http://pypi.python.org/pypi/byeHTML/',
        description='Aims to extract the content from a HTML page.',
        long_description=open('README.md').read()
)

