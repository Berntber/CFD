import os
from setuptools import setup, find_packages

ver_file = os.path.join('ofblockmeshdicthelper', 'version.py')
vars = {}
exec(open(ver_file).read(), vars)

setup(
    name='ofblockmeshdicthelper',
    version=vars['__version__'],
    description='Helper utilities for OpenFOAM blockMeshDict generation.',
    long_description=open('README.rst', 'rt').read(),
    author='Takaaki AOKI',
    author_email='aoki.takaaki@gmail.com',
    url='https://github.com/takaakiaoki/ofblockmeshdicthelper',
    packages=find_packages(),
    package_dir={'ofblockmeshdicthelper': 'ofblockmeshdicthelper'},
    install_requires=['six'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics"])
