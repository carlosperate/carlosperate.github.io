#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys
this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)
print("Import configuration file from: %s" % this_dir)
from pelicanconf import *

SITEURL = '//www.embeddedlog.com'
RELATIVE_URLS = False

# Feed only really needed for publishing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = 'feeds/feed.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Normal config has this probably already configured as True
DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
GOOGLE_ANALYTICS = 'UA-58081399-1'

print("Publish configuration loaded succesfully")
