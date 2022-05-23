from pokeretriever.Ability import Ability
from pokeretriever.PokedexRequestFactory import PokedexRequestFactory
import aiohttp
import asyncio


class AbilityRequestFactory(PokedexRequestFactory):
    """
    Factory class for the Pokemon Ability Request which inherits form PokedexRequestFactory.
    """
    def __init__(self):
        """
        Initializer for the Pokemon Ability Request Factory.
        """
        super().__init__()

    @staticmethod
    async def process_single_request(single_name_or_id: str):
        """
        Async static method that processes a single request.
        :param single_name_or_id: string
        :return: Ability
        """
        url = "https://pokeapi.co/api/v2/ability/{}/"
        async with aiohttp.ClientSession() as session:
            response = await PokedexRequestFactory.get_pokemon_data(single_name_or_id, url, session)
            if response == "An error occurred. Skipping this request.":
                return "An error occurred. Skipping this request."
            ability_name = response.get("name")
            ability_id = response.get("id")
            generation = response.get("generation").get("name")
            effect = response.get("effect_entries")[1].get("effect")
            effect_short = response.get("effect_entries")[1].get("short_effect")
            list_of_pokemon = [pokemon.get("pokemon").get("name") for pokemon in response.get("pokemon")]
            return Ability(ability_name, ability_id, generation, effect, effect_short, list_of_pokemon)

    @staticmethod
    async def process_requests(list_of_ids_or_names: list) -> list:
        """
        Async static method that processes the requests.
        :param list_of_ids_or_names: list
        :return: Ability list
        """
        url = "https://pokeapi.co/api/v2/ability/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [PokedexRequestFactory.get_pokemon_data(ability_id, url, session)
                                for ability_id in list_of_ids_or_names]
            responses = await asyncio.gather(*async_coroutines)
            abilities_list = []
            for counter in range(len(responses)):
                if responses[counter] == "An error occurred. Skipping this request.":
                    abilities_list.append("An error occurred. Skipping this request.")
                else:
                    ability_name = responses[counter].get("name")
                    ability_id = responses[counter].get("id")
                    generation = responses[counter].get("generation").get("name")
                    effect = responses[counter].get("effect_entries")[1].get("effect")
                    effect_short = responses[counter].get("effect_entries")[1].get("short_effect")
                    list_of_pokemon = [pokemon.get("pokemon").get("name")
                                       for pokemon in responses[counter].get("pokemon")]
                    abilities_list.append(Ability(ability_name, ability_id, generation,
                                                  effect, effect_short, list_of_pokemon))
            return abilities_list
