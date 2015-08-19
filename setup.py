import os
from setuptools import setup
# from setuptools.command.install_scripts import install_scripts as _install_scripts
import traceback
import subprocess

version = '0.0.1'


setup(
    

    name='utils',
    version = version,
    
    author = "Ritesh Agrawal",
    author_email = "ragrawal@gmail.com",
    
    description = ("General utility functions"),
    long_description="Date utils",

    packages=['utils']
    
    
)
