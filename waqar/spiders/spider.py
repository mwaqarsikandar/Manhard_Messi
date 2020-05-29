import scrapy
class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.manhard.eu']
    start_urls = ['http://www.manhard.eu/webshop.asp?pa_id=59&level=2&product=002&pagename=messen.html']
    # New 'base_url' variable
    base_url = 'http://www.manhard.eu/webshop.asp'
    


    def parse(self, response):
        

        all_item = response.xpath('//a[@class="wit" and 1]/@href')
        
        for item in all_item:
            item_url = self.base_url
            item_urla = item_url + item.extract()
            for subitem in all_item:
                item_url1 = self.base_url
                item_urla1 = item_url + subitem.extract()
                yield scrapy.Request(item_urla1, callback=self.parse_book)
                
              
                
                
                
            
            

           # for cat in all_books:
           #     book_url1 = self.start_urls[0].replace('?pa_id=59', '')
           #     book_urla1 = book_url1 + cat.extract_first().replace('amp;', '')
           #     for cat1 in all_books:
           #         book_url2 = self.start_urls[0].replace('?pa_id=59', '')
           #         book_urla2 = book_url1 + cat1.extract_first().replace('amp;', '')
           #         yield scrapy.Request(book_urla2, callback=self.parse_book)
                
            
            

            
    def parse_book(self, response):
        title = response.xpath('//td/h1[1]/text()').extract_first()
        relative_image = response.xpath('//td[1]/img[1]/@src').extract_first()
        final_image = self.base_url + relative_image
       
        yield {
            'Title': title,
            'Image': final_image,
          
            
        }
