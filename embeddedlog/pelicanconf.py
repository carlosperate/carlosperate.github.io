#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from distutils.version import LooseVersion
import datetime
from pelican import __version__ as pelican_version

# Check version of Pelican
if LooseVersion(pelican_version) < LooseVersion('3.7.0'):
    print('Please upgrade Pelican to a version >= 3.7')
    exit(1)

# This variable is used for debug purposes
LOCALHOST_ABSOLUTE = True

# Website data
AUTHOR = u'carlosperate'
SITENAME = u'Embedded Log'
TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'
LOCALE = 'C'
DEFAULT_LANG = u'en'
BUILD_YEAR = datetime.datetime.now().year

# Paths data
if LOCALHOST_ABSOLUTE is True:
    SITEURL = 'http://localhost:8080'
    RELATIVE_URLS = False
else:
    SITEURL = ''
    RELATIVE_URLS = True
PATH = 'content'
STATIC_PATHS = ['images']
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']

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
IGNORE_FILES = ['README.md']

# Categories data
#CATEGORY_URL = '{category}/{slug}.html'
#CATEGORY_SAVE_AS = '{category}/{slug}.html'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Blog'
SUMMARY_MAX_LENGTH = 50

# Banner/Carousel in pages
BANNER_ALL_PAGES = True
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'This is my subtitle'

# General navigation
DEFAULT_PAGINATION = 5
DISPLAY_BREADCRUMBS = True

# Internal Pelican cache speeds up build time
LOAD_CONTENT_CACHE = False

# Markdown settings: http://pythonhosted.org/Markdown/reference.html#markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Plugin settings
PLUGIN_PATHS = ['plugins', '../plugins']
PLUGINS = [
    'related_posts',
    'pelican_youtube',
    'embed_tweet'
]
# Still need to pip install typogrify
TYPOGRIFY = False

# Plugin: Related Posts
RELATED_POSTS_MAX = 5

# Plugin: YouTube, manually created variable
PLUGIN_YOUTUBE_ADD_CSS = True

# Theme options
THEME = '../themes/embeddedlog-theme'
THEME_STATIC_DIR = 'theme'
BOOTSTRAP_THEME = 'flatly'
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

# CC license offered by the bootstrap theme
CC_LICENSE = 'CC-BY'

# GitHub active repositories (included in bootstrap theme)
GITHUB_USER = 'carlosperate'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Twitter timeline (included in bootstrap theme) (deprecated)
TWITTER_WIDGET_ID = None

# Facebook/Twitter Cards (included in bootstrap theme)
USE_OPEN_GRAPH = True
TWITTER_CARDS = True
TWITTER_USERNAME = 'carlosperate'

# Share buttons (Shariff included in bootstrap theme)
SHARIFF = True
SHARIFF_LANG = 'en'
SHARIFF_SERVICES = '[&quot;twitter&quot;,&quot;facebook&quot;,&quot;googleplus&quot;,&quot;whatsapp&quot;]'

# Testing stuff
ABOUT_ME = True

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
FEED_RSS = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None

print('Pelican configuration loaded successfully')
