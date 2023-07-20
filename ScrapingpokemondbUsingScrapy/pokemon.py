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
            for row in response.css("table.data-table sticky-header block-wide tr"):
                 print(response)
                 Number=row.css("td.cell-num cell-fixed::text").get()
                 print(Number)
                 Name=row.css("a.ent-name::text").get()
                 print(Name)
                 Type=row.css("td.cell-icon::text").get()
                 print(Type)
                 total=row.css("td.cell-num cell-total::text").get()
                 print(total)
                 HP=row.css("td.cell-num::text").get()
                 print(HP)
                 Attack=row.css("td.cell-num::text").get()
                 print(Attack)
                 Defence=row.css('td.cell-num::text').get()
                 print(Defence)
                 speed_atk=row.css('td.cell-num::text').get()
                 print(speed_atk)
                 speed_def=row.css('td.cell-num::text').get()
                 print(speed_def)
                 speed=row.css('td.cell-num::text').get()
                 print(speed)

                 yield{
                      'Number':Number,
                      'Name':Name,
                      'Type':type,
                      'total':total,
                      'HP':HP,
                      'Attack':Attack,
                      'Defence':Defence,
                      'speed_Atk':speed_atk,
                      'speed_def':speed_def,
                      'speed':speed
                

                 }

                     
       