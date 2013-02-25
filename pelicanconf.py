#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Marco D. Adelfio'
SITENAME = u'Marco D. Adelfio'
SITEURL = ''

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False

# MDA: Remember to restart devserver after making changes here

THEME = 'themes/school-site-simple'
ARTICLE_URL = 'notes/{slug}'
ARTICLE_SAVE_AS = 'notes/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'

DEFAULT_DATE_FORMAT = '%b %d, %Y'

MENUITEMS = [
    ('Projects', '/projects'),
    ('Publications', '/publications'),
    ('Notes', '/notes'),
    ('Demos', '/demos'),
    ('Research', '/research'),
    ('Writing', '/writing'),
    ('Random', '/random'),
    ('Links', '/links'),
    ('About', '/about')
]

DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['files', 'papers']

CSS_FILE = 'marco.css'
