import scrapy
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class SpiderSpider(CrawlSpider):

"""
class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.manhard.eu']
    start_urls = [
        'http://www.manhard.eu/webshop.asp?pa_id=59&level=2&product=002&pagename=messen.html']
    
    base_url = 'http://www.manhard.eu/webshop.asp'
    base_url1 = 'http://www.manhard.eu/'
    #headers= {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    """
    rules = (
        Rule(LinkExtractor(
            allow=r'.*?pa_id=59&.*'), callback='parse_f', follow=True),
         )
    
    def parse_item(self, response):
    http://www.manhard.eu/webshop.asp?pa_id=59&level=4&product=002004021017&pagename=koksmes.html
    """
    def parse(self, response):
        links = response.xpath('//a[@class="wit" and 1]/@href')
        for link in links:
            link1 = self.base_url + link.extract()
            yield scrapy.Request(link1, callback=self.parse_s1)
        """    
        link1 = "http://www.manhard.eu/webshop.asp?pa_id=59&level=4&product=002001001002&pagename=gebogen.html"
        yield scrapy.Request(link1, callback=self.parse_f)
        
        links = response.xpath('//a[@class="wit" and 1]/@href')
        for link in links:
            link1 = self.base_url + link.extract()
        """    
            
            



        

        
        
            
            
            

        
    def parse_s1(self, response):
        linkss1 = response.xpath('//a[@class="wit" and 1]/@href')
        for link in linkss1:
            link1s1 = self.base_url + link.extract()
            yield scrapy.Request(link1s1, callback=self.parse_s2)
            


    def parse_s2(self, response):
        linkss2 = response.xpath('//a[@class="wit" and 1]/@href')
        for link in linkss2:
            link1s2 = self.base_url + link.extract()
            yield scrapy.Request(link1s2, callback=self.parse_f)

        
    def parse_f(self, response):

        
        
        src = response.xpath('//img[@border="0"]/@src')[3].extract()
        src1 = self.base_url1 + src
        tit = response.xpath('//td/h1[1]//text()')[0].extract()
        main = response.xpath('//td[@width="638"]//text()')[3].extract()
        sub1 = response.xpath('//td[@width="638"]//text()')[5].extract()
        sub2 = response.xpath('//td[@width="638"]//text()')[7].extract()
        
        
        if len(response.xpath('//tr[' + str(2) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else:
            
        
            des = response.xpath('//tr[' + str(2) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(2) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(2) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(2) + ']/td[8]//text()')[0].extract()

                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        if len(response.xpath('//tr[' + str(3) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else:
            
        
            des = response.xpath('//tr[' + str(3) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(3) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(3) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(3) + ']/td[8]//text()')[0].extract()


                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        if len(response.xpath('//tr[' + str(4) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else:    
            
            
        
            des = response.xpath('//tr[' + str(4) + ']/td[4]//text()')[1].extract()
            
            
            col = response.xpath('//tr[' + str(4) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(4) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(4) + ']/td[8]//text()')[0].extract()


                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        if len(response.xpath('//tr[' + str(5) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else: 
            
        
            des = response.xpath('//tr[' + str(5) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(5) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(5) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(5) + ']/td[8]//text()')[0].extract()

                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        if len(response.xpath('//tr[' + str(6) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else:
        
            des = response.xpath('//tr[' + str(6) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(6) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(6) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(6) + ']/td[8]//text()')[0].extract()

                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        if len(response.xpath('//tr[' + str(7) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else: 
            
        
            des = response.xpath('//tr[' + str(7) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(7) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(7) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(7) + ']/td[8]//text()')[0].extract()


                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        if len(response.xpath('//tr[' + str(8) + ']/td[4]//text()').extract()) == 0:
            print("List is Empty")
        else:
            
        
            des = response.xpath('//tr[' + str(8) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(8) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(8) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(8) + ']/td[8]//text()')[0].extract()

                            
            yield {
                'Image Link' : src1,
                'Title' : tit,
                'Description' : des,
                'Main Category' : main,
                'Sub Category 1' : sub1,
                'Sub Category 2' : sub2,
                'color': col,
                'Measure' : mea,
                'price' : pri
                
                }
        """        
                    
        col = response.xpath('//tr[2]/td[5]//text()')[1].extract()
        mea = response.xpath('//tr[2]/td[6]//text()')[1].extract()
        pri = response.xpath('//tr[2]/td[8]//text()')[1].extract()
        des = response.xpath('//tr[2]/td[4]//text()')[1].extract()

        #if response.xpath('//tr[' + str(2) + ']/td[4]//text()')[1].extract():
            
            
        
            

                            
        yield {
            
                    
            'Category': des,
            'Item' : tit,
            'Category' : col,
            'Measure' : mea,
            'price' : pri,
            'Image Link' : src1
            }
        """
        """
        if response.xpath('//tr[' + str(4) + ']/td[4]//text()')[1].extract():
            
            
        
            des = response.xpath('//tr[' + str(4) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(4) + ']/td[5]//text()')[0].extract()
            mea = response.xpath('//tr[' + str(4) + ']/td[6]//text()')[0].extract()
            pri = response.xpath('//tr[' + str(4) + ']/td[8]//text()')[0].extract()

                            
            yield {
                    
                'Category': des,
                'Item' : tit,
                'Category' : col,
                'Measure' : mea,
                'price' : pri,
                'Image Link' : src1
                }

        if response.xpath('//tr[' + str(5) + ']/td[4]//text()')[1].extract():
            
            
        
            des = response.xpath('//tr[' + str(5) + ']/td[4]//text()')[1].extract()
            
            col = response.xpath('//tr[' + str(5) + ']/td[5]//text()')[1].extract()
            mea = response.xpath('//tr[' + str(5) + ']/td[6]//text()')[1].extract()
            pri = response.xpath('//tr[' + str(5) + ']/td[8]//text()')[1].extract()

                            
            yield {
                    
                'Category': des,
                'Item' : tit,
                'Category' : col,
                'Measure' : mea,
                'price' : pri,
                'Image Link' : src1
                }

        
        

        


        """    
        """    
        tit = response.xpath('//td/h1[1]//text()')[0].extract()  
           
        for var in self.i3:
            
            try:
                
                            
                des = response.xpath('//tr[' + str(var) + ']/td[4]//text()')[1].extract()
                col = response.xpath('//tr[' + str(var) + ']/td[5]//text()')[1].extract()
                mea = response.xpath('//tr[' + str(var) + ']/td[6]//text()')[1].extract()
                pri = response.xpath('//tr[' + str(var) + ']/td[8]//text()')[1].extract()

                
                yield {
                    
                    'Category': des,
                    'Item' : tit,
                    'Category' : col,
                    'Measure' : mea,
                    'price' : pri,
                    'Image Link' : src1
                    }

            except IndexError:
                print("a is greater than b")
        
            

        

            col = response.xpath('//tr[' + str(2) + ']/td[5]//text()')[1].extract()
            mea = response.xpath('//tr[' + str(2) + ']/td[6]//text()')[1].extract()
            pri = response.xpath('//tr[' + str(2) + ']/td[8]//text()')[1].extract()

        i3 = 2
        while i3 < 9:
            des = response.xpath('//tr[' + str(i3) + ']/td[4]//text()')[1].extract()
            i3 += 1
        """    
              
            
        
        
        
            

    

            

            

        """    

        items = response.xpath('//a[@class="wit" and 1]/text()')
        for item in items:
            item1 = item.extract()
            images = response.xpath('//td[1]/img[1]/@src')
            for image in images:
                image1 = self.base_url1 + image.extract()
                links = response.xpath('//a[@class="wit" and 1]/@href')
                for link in links:
                    link1 = self.base_url + link.extract()

                    response.xpath('//tr[3]/td[@width="235"]//text()').extract()
        """


        """        
        title = response.xpath('//td/h1[1]/text()').extract_first()

        items = response.xpath('//a[@class="wit" and 1]/text()')
        for item in items:
            item1 = item.extract()

        links = response.xpath('//a[@class="wit" and 1]/@href')
        for link in links:
            link1 = self.base_url + link.extract()
            return Request(url=link1,
               callback=self.parse_sub1)
        

        images = response.xpath('//td[1]/img[1]/@src')
        for image in images:
            image1 = self.base_url1 + image.extract()
        """

        """        
                        
        def parse_sub1(self, response):
            title = response.xpath('//td/h1[1]/text()').extract_first()

            items = response.xpath('//a[@class="wit" and 1]/text()')
            for item in items:
                item1 = item.extract()

            links = response.xpath('//a[@class="wit" and 1]/@href')
            for link in links:
                link1 = self.base_url + link.extract()
                return Request(url=link1,
                   callback=self.parse_sub2)
            

            images = response.xpath('//td[1]/img[1]/@src')
            response.xpath('//tr[2]/td[4]').extract()
            for image in images:
                image1 = self.base_url1 + image.extract()

            

            yield {
                'Title': title,
                'Item' : item1,
                'Image': image1,
                'Link' : link1,
            }

                
        def parse_sub2(self, response):
            title = response.xpath('//td/h1[1]/text()').extract_first()

            items = response.xpath('//a[@class="wit" and 1]/text()')
            for item in items:
                item1 = item.extract()

            links = response.xpath('//a[@class="wit" and 1]/@href')
            for link in links:
                link1 = self.base_url + link.extract()
                return Request(url=link1,
                   callback=self.page_parse)
            

            images = response.xpath('//td[1]/img[1]/@src')
            for image in images:
                image1 = self.base_url1 + image.extract()

            

            yield {
                'Title': title,
                'Item' : item1,
                'Image': image1,
                'Link' : link1,
            }


        def parse_sub3(self, response):
            title = response.xpath('//td/h1[1]/text()').extract_first()

            items = response.xpath('//a[@class="wit" and 1]/text()')
            for item in items:
                item1 = item.extract()

            links = response.xpath('//a[@class="wit" and 1]/@href')
            for link in links:
                link1 = self.base_url + link.extract()
                return Request(url=link1,
                   callback=self.page_parse)
            

            images = response.xpath('//td[1]/img[1]/@src')
            for image in images:
                image1 = self.base_url1 + image.extract()

            

            yield {
                'Title': title,
                'Item' : item1,
                'Image': image1,
                'Link' : link1,
            }
            

                
            
                
                

           
            
          
            items = response.xpath('//a[@class="wit" and 1]/text()')
            for item in items:
                item1 = item.extract()
                images = response.xpath('//td[1]/img[1]/@src')
                for image in images:
                    image1 = self.base_url1 + image.extract()
                    links = response.xpath('//a[@class="wit" and 1]/@href')
                    for link in links:
                        link1 = self.base_url + link.extract()
                        
                    
                    yield {
                        'Title': title,
                        'Item' : item1,
                        'Image': image1,
                        'Link' : link1,
                    }
        """
                    

                        
            
            
            
            

            

