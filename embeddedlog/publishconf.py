#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys

# Importing all the configuration from pelicanconf.py
this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)
print('Import configuration file from: {}'.format(this_dir))
from pelicanconf import *

# Rewriting settings from pelicanconf.py
SITEURL = '//www.embeddedlog.com'
RELATIVE_URLS = False

# Feeds only really needed for publishing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = 'feeds/feed.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Ensure a clean build
DELETE_OUTPUT_DIRECTORY = True

# We don't want any cookies or user tracking
GOOGLE_ANALYTICS = None

print('PUBLISH configuration loaded successfully')
