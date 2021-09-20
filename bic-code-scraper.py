# scrapy runspider bic-code-scraper.py -O bic.csv
import scrapy

class BICCodeSpider(scrapy.Spider):
    name = 'BIC Code'
    start_urls = [
        'https://www.bic-code.org/bic-letter-search/?resultsperpage=10000',
    ]

    def parse(self, response):
        for bic in response.xpath('//*[@class="bic-result-table"]/table/tbody/tr'):
            yield {
                'Code': bic.xpath('td[@data-label="Code"]/text()').get(),
                'Company': bic.xpath('td[@data-label="Company"]/text()').get(),
                'City': bic.xpath('td[@data-label="City"]/text()').get(),
                'Country': bic.xpath('td[@data-label="Country"]/text()').get(),
            }
