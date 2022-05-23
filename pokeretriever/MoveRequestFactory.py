from pokeretriever.Move import Move
from pokeretriever.PokedexRequestFactory import PokedexRequestFactory
import aiohttp
import asyncio


class MoveRequestFactory(PokedexRequestFactory):
    """
    Class representation of the Pokemon's Move Request Factory,
     which inherits from PokedexRequestFactory.
    """
    def __init__(self):
        super().__init__()

    @staticmethod
    async def process_single_request(single_name_or_id: str):
        """
        Async static method that processes a single request.
        :param single_name_or_id: string
        :return: PokedexObject
        """
        url = "https://pokeapi.co/api/v2/move/{}/"
        async with aiohttp.ClientSession() as session:
            response = await PokedexRequestFactory.get_pokemon_data(single_name_or_id, url, session)
            if response == "An error occurred. Skipping this request.":
                return "An error occurred. Skipping this request."
            move_name = response.get("name")
            move_id = response.get("id")
            generation = response.get("generation").get("name")
            accuracy = response.get("accuracy")
            pp = response.get("pp")
            power = response.get("power")
            move_type = response.get("type").get("name")
            damage_class = response.get("damage_class").get("name")
            short_effect = response.get("effect_entries")[0].get("short_effect")
            return Move(move_name, move_id, generation, accuracy, pp, power, move_type, damage_class, short_effect)

    @staticmethod
    async def process_requests(list_of_ids_or_names: list) -> list:
        """
        Async static method that processes the requests.
        :param list_of_ids_or_names: list
        :return: PokedexObject list
        """
        url = "https://pokeapi.co/api/v2/move/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [PokedexRequestFactory.get_pokemon_data(ability_id, url, session)
                                for ability_id in list_of_ids_or_names]
            responses = await asyncio.gather(*async_coroutines)
            moves_list = []
            for counter in range(len(responses)):
                if responses[counter] == "An error occurred. Skipping this request.":
                    moves_list.append("An error occurred. Skipping this request.")
                else:
                    move_name = responses[counter].get("name")
                    move_id = responses[counter].get("id")
                    generation = responses[counter].get("generation").get("name")
                    accuracy = responses[counter].get("accuracy")
                    pp = responses[counter].get("pp")
                    power = responses[counter].get("power")
                    move_type = responses[counter].get("type").get("name")
                    damage_class = responses[counter].get("damage_class").get("name")
                    short_effect = responses[counter].get("effect_entries")[0].get("short_effect")
                    moves_list.append(Move(move_name, move_id, generation, accuracy,
                                           pp, power, move_type, damage_class, short_effect))
            return moves_list
