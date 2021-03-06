#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://umiacs.umd.edu/~marco'

DELETE_OUTPUT_DIRECTORY = True
LINK_LOCAL_JAVASCRIPT = False

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

MENUITEMS = [
    ('Publications', SITEURL + '/publications'),
    ('Projects', SITEURL + '/projects'),
    #('Notes', SITEURL + '/notes'),
    ('Links', SITEURL + '/links'),
    ('About', SITEURL + '/about')
]

GOOGLE_ANALYTICS = 'UA-9669059-5'
STATCOUNTER = [8544392, 'd727ef73']

