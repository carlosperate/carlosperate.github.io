#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""
This file is only used if you use `make publish` or explicitly specify it as
your config file.

All the setting changes are contained inside pelicanconf.py, but this file
sets the Build Mode before importing it, which alters the configuration for
deployment.
"""
from __future__ import unicode_literals
import os
import sys

this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)
from pelicanbuildmode import set_build_mode, BuildMode
set_build_mode(BuildMode.PUBLISH)

print('Import configuration file from: {}'.format(this_dir))
from pelicanconf import *

print('PUBLISH configuration loaded successfully')
