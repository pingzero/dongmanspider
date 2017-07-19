import scrapy
from ..items import DongmanItem
class fspiderSpider(scrapy.Spider):
    name="dongman"
    start_urls=['http://news.dmzj.com/']
    def parse(self,response):
        item=DongmanItem()
        title=response.xpath(".//div[@class='briefnews_con_li']/div[2]/h3/a/text()").extract()
        img=response.xpath(".//div[@class='briefnews_con_li']/div[1]/a/img/@src").extract()
        for t,i in zip(title,img):
            item['title']=t
            item['img']=i
            yield item
