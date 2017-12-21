# -*- coding: utf-8 -*-
import scrapy
import urllib
import sys


def start_requests(self):
    params_dict = {
        'cx': ['partner-pub-9634067433254658:5laonibews6'],
        'cof': ['FORID:10'],
        'ie': ['ISO-8859-1'],
        'q': ['query'],
        'sa.x': ['0'],
        'sa.y': ['0'],
        'sa': ['Search'],
        'ad': ['n9'],
        'num': ['10'],
        'rurl': [
            'http://www.blogsearchengine.org/search.html?cx=partner-pub'
            '-9634067433254658%3A5laonibews6&cof=FORID%3A10&ie=ISO-8859-1&'
            'q=query&sa.x=0&sa.y=0&sa=Search'
        ],
       # 'siteurl': ['http://www.blogsearchengine.org/']
        'siteurl': ['http://www.jianshu.com/']
    }
    params = urllib.parse.urlencode(params  _dict, doseq=True)
    url_template = urllib.parse.urlunparse(
        ['https', self.allowed_domains[0], '/cse',
         '', params, 'gsc.tab=0&gsc.q=query&gsc.page=page_num'])
    for query in self.queries:
        for page_num in range(1, 11):
            url = url_template.replace('query', urllib.parse.quote(query))
            url = url.replace('page_num', str(page_num))
            yield SplashRscequest(url, self.parse, endpoint='render.html',
                                args={'wait': 0.5})