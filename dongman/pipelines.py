# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import pymysql
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
class DongmanPipeline(ImagesPipeline):
    def file_path(self,request,response=None,info=None):
        image_guid=requset.url.spider('/')[-1]
        return 'full/%s' %(images_guid)
    def get_media_requests(self,item,info):
        self.con=pymysql.Connect(user='root',password='zero',db='tests',charset='UTF8')
        self.cu=self.con.cursor()
        title=item['title']
        img=item['img']
        value=[title,img]
        insert_sql='replace into datail (title,img) values(%s,%s)'
        self.cu.execute(insert_sql,value)
        self.con.commit()
        yield Request(img)
    def item_completed(self,results,item,info):
        images_paths=[x['path'] for ok,x in results if ok]
        self.con.close()
        if not images_paths:
            raise DropItem('Item contains no images')
        return item
