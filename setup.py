import setuptools
from distutils.core import setup
from codecs import open
from os import path


setuptools.setup(
    name="IRModule",
    setup_requires=["setuptools_scm"],
    description="Python (2 or 3) module for receiving IR remote control signals (NEC format) on a Raspberry Pi using a TSOP382 IR Receiver",
    author="owainm713",
    license="GNU General Public License v3.0",
    packages=setuptools.find_packages()
)