from os import path
from setuptools import  setup
from setuptools import find_namespace_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

setup(
    name='my_pgs'
    version='1.0',
    long_description=long_description,
    long_description_content_type='tesxt/markdown',
    url='http;//gite.my_rep',
    auther='z31',
    auther_email='z31@gmail.com'

    install_requires=[
        'flask'
        'prettytable'
    ],


)