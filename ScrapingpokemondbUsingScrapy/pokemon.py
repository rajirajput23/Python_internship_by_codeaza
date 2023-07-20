import scrapy
from pathlib import Path

class PokemonSpider(scrapy.Spider):
    name = "pokemon"
    allowed_domains = ["pokemondb.net"]
    start_urls = ["https://pokemondb.net/"]

   
    def start_requests(self):
        urls = [
            "https://pokemondb.net/pokedex/all"  
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
            #table=response.css('table.data-table sticky-header block-wide')
            #print(table)
            #rows=response.css('table.data-table sticky-header block-wide ')
            #print(rows)
            for row in response.css("table.data-table sticky-header block-wide  tr"):
                 Number=row.css("td.cell-num cell-fixed::text").get()
                 print(Number)
                     
       