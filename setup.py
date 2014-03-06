# encoding: utf-8

'''
@author:     Jose Emilio Romero Lopez

@copyright:  2013 organization_name. All rights reserved.

@license:    LGPL

@contact:    jemromerol@gmail.com

  This file is part of AMPAPicker.

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from setuptools import setup
from setuptools import find_packages
import re


def get_version_number():
    VERSIONFILE = "eqpickertool/_version.py"
    verstrline = open(VERSIONFILE, "rt").read()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
    return verstr

setup(name="EQ Picker Tool",
      version=get_version_number(),
      description="A set of tools to perform seismic event detection and picking",
      author="Jose Emilio Romero Lopez",
      author_email="jemromerol@gmail.com",
      url="",
      license="LGPL",
      scripts=["bin/detector.py", "bin/generator.py", "bin/detectorgui.py"],
      install_requires=['numpy > 1.7', 'scipy >= 0.13', 'matplotlib', 'PySide'],
      packages=find_packages()
      )

