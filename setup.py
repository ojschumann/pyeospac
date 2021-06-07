#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, Extension, find_packages
import os.path
from Cython.Distutils import build_ext
from configparser import ConfigParser
from setup_eospac import setup_eospac
from setup_feos import setup_feos
import re

# a define the version sting inside the package
# see https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package 
VERSIONFILE="eospac/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

cfg_obj = ConfigParser()
cfg_obj.read('setup.cfg')
cfg_eospac = dict(cfg_obj.items('EOSPAC'))
cfg_feos = dict(cfg_obj.items('FEOS'))

warning_sign =   ''.join([ "="*80, "\n",
                           ' '*10, '{0}',
                           "="*80, "\n"])
extensions_found = []
if os.path.exists(cfg_eospac['path']):
    extensions_found += setup_eospac(cfg_eospac)
else:
    print(warning_sign.format('Warning: linking to the EOSPAC library was not done. '))

if os.path.exists(cfg_feos['path']):
    extensions_found += setup_feos(cfg_feos)
else:
    print(warning_sign.format('Warning: linking to the EOSPAC library was not done. '))

setup(
    name="eospac",
    version=version,
    author='Roman Yurchak',
    author_email='rth@crans.org',
    packages=find_packages(),
    cmdclass={'build_ext': build_ext},
    ext_modules=extensions_found,
    entry_points = {
        #'console_scripts': [ 'eostab2vtk = eospac.viz:convert_to_vtk' ]
        },
    tests_require=['nose']
)


