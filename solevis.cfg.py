# -*- coding: utf-8 -*-

AUTHOR = "solevis"
SITENAME = u"/home/solevis"
SITEURL = "http://www.solevis.net"
TIMEZONE = "Europe/Paris"

PDF_GENERATOR = False
DEFAULT_PAGINATION = 4

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS=(
        ('rhaamo', 'http://rhaamo.li/'),
        ('llew', 'http://www.llew.me/'),
        ('orgrim', 'http://orgrim.net/'),
        ('guigui2', 'http://www.guigui2.net/dotclear/'),
        ('philpep', 'http://blog.philpep.org/'),
        ('jpcw', 'http://jp.camguilhem.net/'),
        ('paulla', 'http://www.paulla.asso.fr/'),
        ('netbsdfr', 'http://www.netbsdfr.org/'),
        ('gcu', 'http://gcu.info/'),
)

SOCIAL = (\
          ('twitter', 'http://twitter.com/solevis'),\
          ('github', 'https://github.com/solevis/'),\
          ('linkedin', 'fr.linkedin.com/pub/sylvain-mora/5b/678/673'),)

STATIC_PATHS = ["patchs", "docs",]

DEFAULT_LANG="fr"
DISPLAY_PAGES_ON_MENU=True
DISQUS_SITENAME="homesolevis"
THEME="tuxlite_tbs-fr"

GOOGLE_ANALYTICS="UA-21064931-1"

PIWIK_URL="piwik.solevis.net"
PIWIK_SITE_ID="1"

# DEBUG
RELATIVE_URLS = True
