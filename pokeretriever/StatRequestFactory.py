from pokeretriever.PokedexRequestFactory import PokedexRequestFactory
import aiohttp
import asyncio
from pokeretriever.Stat import Stat


class StatRequestFactory(PokedexRequestFactory):
    """
    Class representation of the StatFactoryRequest which inherits from PokedexRequestFactory.
    """
    def __init__(self):
        """
        Initializer for StatFactoryRequest.
        """
        super().__init__()

    @staticmethod
    async def process_single_request(single_name_or_id: str):
        """
        Async static method that processes a single request.
        :param single_name_or_id: string
        :return: Stat,str
        """
        url = "https://pokeapi.co/api/v2/stat/{}/"
        async with aiohttp.ClientSession() as session:
            response = await PokedexRequestFactory.get_pokemon_data(single_name_or_id, url, session)
            if response == "An error occurred. Skipping this request.":
                return "An error occurred. Skipping this request."
            stat_name = response.get("name")
            stat_id = response.get("id")
            is_battle_only = response.get("is_battle_only")
            return Stat(stat_name, stat_id, is_battle_only)

    @staticmethod
    async def process_requests(list_of_ids_or_names: list) -> list:
        """
        Async static method that processes the requests.
        :param list_of_ids_or_names: list
        :return: Stat list
        """
        url = "https://pokeapi.co/api/v2/stat/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [PokedexRequestFactory.get_pokemon_data(ability_id, url, session)
                                for ability_id in list_of_ids_or_names]
            responses = await asyncio.gather(*async_coroutines)
            stats_list = []
            for counter in range(len(responses)):
                if responses[counter] == "An error occurred. Skipping this request.":
                    stats_list.append("An error occurred. Skipping this request.")
                else:
                    stat_name = responses[counter].get("name")
                    stat_id = responses[counter].get("id")
                    is_battle_only = responses[counter].get("is_battle_only")
                    stats_list.append(Stat(stat_name, stat_id, is_battle_only))
            return stats_list
