
import scrapy


class PokemonScrapper(scrapy.Spider):
    name = 'pokemon_scrapper'
    domain = 'https://bulbapedia.bulbagarden.net'
    start_urls = [
	    "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"]

    pokemonClass = {
                "name" : "",
                "ndex" : "",
                "height" : "",
                "weight" : "",
                "color": "",
                "type1": "",
                "type2": ""
            }

    def parse(self, response):
        pokemons = response.css('tr')
        
        for pokemon in pokemons:

            pokemon_url = pokemon.css('td>a::attr(href)').get()
            
            if pokemon_url is not None:
                yield response.follow(self.domain + pokemon_url, self.parse_pokemon)

    def parse_pokemon(self, response):
        
        self.pokemonClass["name"] = response.css('td big big b::text').get()
        self.pokemonClass["ndex"] = response.xpath('string(/html/body/div[2]/div[1]/div[2]/div[6]/div[4]/div/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/th/big/big/a/span)').re(r"#\d+")[0]
        self.pokemonClass["height"] = response.xpath('string(//*[@id="mw-content-text"]/div/table[2])').re(r"\d+\.\d+ m")[0]
        self.pokemonClass["weight"] = response.xpath('string(//*[@id="mw-content-text"]/div/table[2])').re(r"\d+\.\d+ kg")[0]
        self.pokemonClass["color"] = response.xpath('string(//a[@title="List of Pokémon by color"]/../../table/tbody/tr/td/text())').get().strip()
        self.pokemonClass["type1"] = response.xpath('string(/html/body/div[2]/div[1]/div[2]/div[6]/div[4]/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[1]/a/span/b)').re(r"\w+")[0]
        self.pokemonClass["type2"] = response.xpath('string(/html/body/div[2]/div[1]/div[2]/div[6]/div[4]/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/a/span/b)').re(r"\w+")[0]
        
        yield self.pokemonClass
        # yield {
        #     'name': response.css('td big big b::text').get(),
        #     'ndex': response.xpath('string(/html/body/div[2]/div[1]/div[2]/div[6]/div[4]/div/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/th/big/big/a/span)').re(r"#\d+")[0],
        #     'height': response.xpath('string(//*[@id="mw-content-text"]/div/table[2])').re(r"\d+\.\d+ m")[0],
        #     'weight': response.xpath('string(//*[@id="mw-content-text"]/div/table[2])').re(r"\d+\.\d+ kg")[0],
        # }
		
