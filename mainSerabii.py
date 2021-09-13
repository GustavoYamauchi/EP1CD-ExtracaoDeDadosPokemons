
import scrapy
import re

class PokemonScrapper(scrapy.Spider):
    name = 'pokemon_scrapper_Serabii'
    domain = 'https://www.serebii.net'
    start_urls = [
	    "https://www.serebii.net/pokemon/ivysaur/"]


    pokemonClass = {
                # "name" : "",
                "ndex" : "", 
                "Normal" : "",
                "Fire" : "",
                "Water" : "",
                "Electric" : "",
                "Grass" : "",
                "Ice" : "",
                "Fighting" : "",
                "Poison" : "",
                "Ground" : "",
                "Flying" : "",
                "Psychic" : "",
                "Bug" : "",
                "Rock" : "",
                "Ghost" : "",
                "Dragon" : "",
                "Dark" : "",
                "Steel" : "",
                "Fairy" : ""
            }

    def parse(self, response):
        navs = ["nav", "nav2", "nav4", "nav5", "nav6", "nav7", "nav8", "nav9"]
        for nav in navs:
            pokemons = response.xpath(f"//form[@name='{nav}']/select/option/@value").getall()
            for pokemon in pokemons:
                if pokemon is not None or pokemon != '#':
                    yield response.follow(self.domain + pokemon, self.pokedex)
        
    def pokedex(self, response):
        pokedex_link = response.xpath('//*[@class="alterdex"]/a/b[text()="Pokédex"]/../@href').get()
        yield response.follow(self.domain + pokedex_link, self.parse_pokemon)
	

    def parse_pokemon(self, response):
        
        # self.pokemonClass["name"] = response.css('td big big b::text').get()
        # self.pokemonClass["name"] = response.xpath('string(/html/body/div[2]/div[2]/main/div[2]/table[1]/tbody/tr/td[1]/table/tbody/tr/td[2]/h1/text())')[0]
        nameNdex = re.search(r"\s(#\d{3})\s([A-Za-z \.]+)", response.css('h1::text').get())
        
        # self.pokemonClass["name"] = nameNdex.group(2)
        self.pokemonClass["ndex"] = nameNdex.group(1)
        self.pokemonClass["Normal"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[1]/text())').re(r"\d+")[0]
        self.pokemonClass["Fire"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[2]/text())').re(r"\d+")[0]
        self.pokemonClass["Water"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[3]/text())').re(r"\d+")[0]
        self.pokemonClass["Electric"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[4]/text())').re(r"\d+")[0]
        self.pokemonClass["Grass"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[5]/text())').re(r"\d+")[0]
        self.pokemonClass["Ice"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[6]/text())').re(r"\d+")[0]
        self.pokemonClass["Fighting"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[7]/text())').re(r"\d+")[0]
        self.pokemonClass["Poison"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[8]/text())').re(r"\d+")[0]
        self.pokemonClass["Ground"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[9]/text())').re(r"\d+")[0]
        self.pokemonClass["Flying"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[10]/text())').re(r"\d+")[0]
        self.pokemonClass["Psychic"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[11]/text())').re(r"\d+")[0]
        self.pokemonClass["Bug"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[12]/text())').re(r"\d+")[0]
        self.pokemonClass["Rock"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[13]/text())').re(r"\d+")[0]
        self.pokemonClass["Ghost"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[14]/text())').re(r"\d+")[0]
        self.pokemonClass["Dragon"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[15]/text())').re(r"\d+")[0]
        self.pokemonClass["Dark"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[16]/text())').re(r"\d+")[0]
        self.pokemonClass["Steel"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[17]/text())').re(r"\d+")[0]
        self.pokemonClass["Fairy"] = response.xpath('string(//h2[text()="Weakness"]/../../../tr[3]/td[18]/text())').re(r"\d+")[0]

        yield self.pokemonClass
		
