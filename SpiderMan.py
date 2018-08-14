# -*- coding: utf-8 -*-
from DataOutput import Dataoutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager

class SpiderMan(object):

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = Dataoutput()

    def crawl(self,root_utl):
        self.manager.add_new_url(root_utl)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print "已经抓取%s个链接" % self.manager.old_url_size()
            except Exception as e:
                # print 'crawl failed'
                print e
        self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E9%9B%AA%E6%B3%A5%E9%B8%BF%E7%88%AA/29339.htm")