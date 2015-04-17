#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Carlos Perate'
SITENAME = u'Embedded Log'
SITEURL = ''
GOOGLE_ANALYTICS = 'UA-58081399-1'

PATH = 'content'
STATIC_PATHS = ['images']

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_ORDER_BY = 'page-order'

#CATEGORY_URL = '{category}/{slug}.html'
#CATEGORY_SAVE_AS = '{category}/{slug}.html'

DEFAULT_PAGINATION = 5

TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

LOAD_CONTENT_CACHE = False

DISPLAY_BREADCRUMBS = True

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'blog'

SUMMARY_MAX_LENGTH = 150

BANNER_ALL_PAGES = True
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'This is my subtitle'

# Menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (('Blog', '/category/blog.html'),
             ('Ardublockly', '/ardublockly/index.html'),
             ('LightUp Alarm', '/LightUp-Alarm/index.html'),
             ('Pebble QuickHue', '/PebbleQuickHue/index.html'),
             ('About', '/about/index.html'),)

# Sidebar
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10
SOCIAL = (('github', 'https://github.com/carlosperate'),
          ('twitter', 'https://twitter.com/carlosperate'),
          ('google+', 'https://plus.google.com/109111328639820363664'),)
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)
#MENUITEMS=(('', '#'))
TWITTER_USERNAME = 'carlosperate'

# Theme options
THEME = '../themes/embeddedlog-theme'
BOOTSTRAP_THEME = 'flatly'
GITHUB_USER = 'carlosperate'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins", "../plugins"]
PLUGINS = ["related_posts"]

RELATED_POSTS_MAX = 5
