#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This variable is used for debug purposes
DEPLOY_RUN = False

# Website data
AUTHOR = u'carlosperate'
SITENAME = u'Embedded Log'
GOOGLE_ANALYTICS = 'UA-58081399-1'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'
CC_LICENSE = 'CC-BY'

# Paths data
if DEPLOY_RUN is True:
    SITEURL = 'http://www.embeddedlog.com'
    RELATIVE_URLS = False
else:
    SITEURL = ''
    RELATIVE_URLS = True
PATH = 'content'
STATIC_PATHS = ['images']

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (('Blog', SITEURL + '/category/blog.html'),
             ('About', SITEURL + '/about/index.html'),)

# Sidebar
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10
#MENUITEMS=(('', '#'))
SOCIAL = (('github', 'https://github.com/carlosperate'),
          ('twitter', 'https://twitter.com/carlosperate'),
          ('google+', 'https://plus.google.com/109111328639820363664'),)
LINKS = (('The Amp Hour podcast', 'http://www.theamphour.com'),
         ('Embedded.fm podcast', 'http://embedded.fm'),)


# Pages data
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_ORDER_BY = 'page-order'

# Categories data
#CATEGORY_URL = '{category}/{slug}.html'
#CATEGORY_SAVE_AS = '{category}/{slug}.html'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Blog'
SUMMARY_MAX_LENGTH = 50

# Both pages and categories
BANNER_ALL_PAGES = True
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'This is my subtitle'

# General navigation
DEFAULT_PAGINATION = 5
LOAD_CONTENT_CACHE = False
DISPLAY_BREADCRUMBS = True

# Share buttons
SHARIFF = True
SHARIFF_LANG = 'en'
SHARIFF_SERVICES = '[&quot;twitter&quot;,&quot;facebook&quot;,&quot;googleplus&quot;,&quot;xing&quot;,&quot;whatsapp&quot;]'

# Twitter Cards
USE_OPEN_GRAPH = True
TWITTER_CARDS = False
TWITTER_USERNAME = None

# Plugins
PLUGIN_PATHS = ["plugins", "../plugins"]
PLUGINS = ["related_posts", "pelican_youtube"]
RELATED_POSTS_MAX = 5

# Theme options
THEME = '../themes/embeddedlog-theme'
BOOTSTRAP_THEME = 'flatly'
GITHUB_USER = 'carlosperate'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
TWITTER_WIDGET_ID = None

# Feed generation is usually not desired when developing
if DEPLOY_RUN is True:
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None
else:
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None
