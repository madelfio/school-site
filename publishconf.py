#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://umiacs.umd.edu/~marco'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

MENUITEMS = [
    ('Projects', SITEURL + '/projects'),
    ('Publications', SITEURL + '/publications'),
    #('Notes', SITEURL + '/notes'),
    ('Links', SITEURL + '/links'),
    ('About', SITEURL + '/about')
]

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
