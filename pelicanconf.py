#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = u'pelican-blueidea'


AUTHOR = u'Iury Sousa'
SITENAME = u'OceanLab'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']


TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python4Oceanographers', 'https://ocefpaf.github.io/python4oceanographers/'),
         ('PyAOS', 'http://pyaos.johnny-lin.com/'),)

# Social widget
GITHUB_URL = 'https://github.com/iuryt'
#SOCIAL = (('GitHub', 'https://github.com/iuryt'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
