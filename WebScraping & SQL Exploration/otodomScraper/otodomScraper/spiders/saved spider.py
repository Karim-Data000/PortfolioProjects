import scrapy
from otodomScraper.items import ListingItem
# from scrapy_splash import SplashRequest

# lua_script = """
# function main(splash, args)
#     assert(splash:go(args.url))

#   while not splash:select('#__next > main > div.css-zcvss2.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div:nth-child(3) > div > div:nth-child(5) > div:nth-child(3)') do
#     splash:wait(0.1)
#     print('waiting...')
#   end
#   return {html=splash:html()}
# end
# """

class RealestateSpider(scrapy.Spider):
    name = "RealEstate"
    allowed_domains = ["otodom.pl"]
    start_urls =  ['https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska'] + [f'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska?page={page}' for page in range(2, 40)] + ['https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska']  + [f'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?page={page}' for page in range(2, 40)]
    # start_urls = ['https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska']  + [f'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?page={page}' for page in range(2, 40)]
    # start_urls =  [f'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?page={page}' for page in range(42, 60)]
    # start_urls =  ['https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/cala-polska?page=50']


    custom_settings = {
    
    'DOWNLOAD_DELAY': 3     # 3 seconds of delay 
    
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url, 
                # endpoint='render.html',
                # args={'wait': 2, 
                #       'headers': {},
                    #   'lua_source': lua_script, 
                    #   url: 'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/cala-polska'
                    # },
                callback=self.parse)

    def parse(self, response):
        listings = response.css('#__next > div.css-1bx5ylf.e50rtj23 > main > div > div.css-1d0gimt.e50rtj21 > div.css-feokcq.e50rtj24 > div.ef1jqb0.css-1cvir3j > div.css-1i43dhb.ef1jqb1 > div:nth-child(4) > ul > li')
        
        print(f'***************************                    *************')
        print(f'***************************  {len(listings):^12}********************')
        print(f'***************************                    **********')

        # with open('trying.txt', 'w', encoding='utf-16') as file:
        #     file.write(response.css('::text').get())
        
        for listing in listings:
            listing_page = listing.css('article > section > div.css-13gthep.eeungyz2 > a::attr(href)').get()
            if listing_page:
                listing_page_url = response.urljoin(listing_page)
                
            yield scrapy.Request(listing_page_url,
                                    # endpoint='render.html',
                                    # args={'wait': 2, 
                                    #     'headers': {},
                                        # 'lua_source': lua_script,
                                        # 'url' : listing_page_url
                                        # },
                                    callback=self.parse_listing)

        
        
        
    def parse_listing(self, response):
        listing_item = ListingItem()

        listing_item['url'] = response.url
        listing_item['title'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > header > h1::text').get()
        listing_item['location'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > header > div > a::text').get()
        listing_item['price'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > header > strong::text').get()
        listing_item['price_per_m2'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > header > div.css-1h1l5lm.e1csqp8m9::text').get()
        # listing_item['estimated_loan_installment'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div.css-1uml5m3.e11wx54m0 > div::text').getall()
        listing_item['area'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div:nth-child(1) > div > div::text').getall()
        listing_item['form_of_ownership'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[0]
        listing_item['rooms'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[2]
        listing_item['finish_condition'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[3]
        listing_item['floor'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[4]
        listing_item['balcony_garden'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[5:6]
        listing_item['rent'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[6:7]
        listing_item['parking_space'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > div > div > div > div:nth-child(3) > div:nth-child(1) ::text').getall()[7:9]
        listing_item['listing_description'] = response.css('#__next > main > div.css-zcvss4.eo3m6aa0 > div.css-y6l269.eo3m6aa3 > section.css-1umupf3.eu82sls0 ::text').getall()[5:-4]
        # listing_item['additional_info']  = additional_info
        
        yield listing_item
