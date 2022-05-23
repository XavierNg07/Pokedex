import abc

import aiohttp


class PokedexRequestFactory(abc.ABC):
    """
    Abstract class representation of a blueprint for PokedexRequestFactory.
    """
    def __init__(self):
        """
        Initializer for PokedexRequestFactory.
        """
        pass

    @staticmethod
    async def get_pokemon_data(single_name_or_id: str, url: str, session: aiohttp.ClientSession):
        """
        Static method which gets the pokemon's data.
        :param single_name_or_id: string
        :param url: string
        :param session: aiohttp.ClientSession
        :return:dictionary, string
        """
        target_url = url.format(single_name_or_id)
        response = await session.request(method="GET", url=target_url)
        if response.status == 200:
            json_dict = await response.json()
            return json_dict
        return "An error occurred. Skipping this request."

    @staticmethod
    @abc.abstractmethod
    async def process_single_request(single_name_or_id: str):
        """
        Abstract static method which processes a single request.
        :param single_name_or_id: string
        :return: PokedexObject
        """
        pass

    @staticmethod
    @abc.abstractmethod
    async def process_requests(list_of_ids_or_names: list) -> list:
        """
        Abstract static method which processes the requests.
        :param list_of_ids_or_names: string
        :return: PokedexObject list
        """
        pass
