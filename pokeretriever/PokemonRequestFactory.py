from pokeretriever.AbilityRequestFactory import AbilityRequestFactory
from pokeretriever.MoveRequestFactory import MoveRequestFactory
from pokeretriever.PokedexRequestFactory import PokedexRequestFactory
import aiohttp
import asyncio
from pokeretriever.Pokemon import Pokemon
from pokeretriever.StatRequestFactory import StatRequestFactory


class PokemonRequestFactory(PokedexRequestFactory):
    """
    Class representation of PokemonRequestFactory which inherits from PokedexRequestFactory
    """
    def __init__(self, expanded: bool):
        """
        Initializer for PokemonRequestFactory.
        :param expanded: bool
        """
        super().__init__()
        self._expanded = expanded

    async def process_single_request(self, single_name_or_id: str) -> Pokemon:
        """
        Async static method that processes a single request.
        :param single_name_or_id: string
        :return: Pokemon
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        async with aiohttp.ClientSession() as session:
            response = await PokedexRequestFactory.get_pokemon_data(single_name_or_id, url, session)
            pokemon_name = response.get("name")
            pokemon_id = response.get("id")
            height = response.get("height")
            weight = response.get("weight")
            types = [pokemon_type.get("type").get("name") for pokemon_type in response.get("types")]
            list_of_abilities_name = [ability.get("ability").get("name") for ability in response.get("abilities")]
            if self._expanded:
                list_of_stats_names = [stat.get("stat").get("name") for stat in response.get("stats")]
                stats_list = await StatRequestFactory.process_requests(list_of_stats_names)
                abilities_list = await AbilityRequestFactory.process_requests(list_of_abilities_name)
                list_of_moves_name = [move.get("move").get("name") for move in response.get("moves")]
                moves_list = await MoveRequestFactory.process_requests(list_of_moves_name)
                pokemon = Pokemon(pokemon_name, pokemon_id, height, weight,
                                  stats_list, types, abilities_list, moves_list)
            else:
                stats = [(stat.get("stat").get("name"), stat.get("base_stat")) for stat in response.get("stats")]
                moves = [('Move name: %s' % (move.get("move").get("name")),
                          'Level acquired: %s' % (move.get("version_group_details")[0].get("level_learned_at")))
                         for move in response.get("moves")]
                pokemon = Pokemon(pokemon_name, pokemon_id, height, weight,
                                  stats, types, list_of_abilities_name, moves)
            pokemon.expanded = self._expanded
            return pokemon

    async def process_requests(self, list_of_ids_or_names: str) -> list:
        """
        Async static method that processes the requests.
        :param list_of_ids_or_names: list
        :return: PokedexObject list
        """
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        async with aiohttp.ClientSession() as session:
            async_coroutines = [PokedexRequestFactory.get_pokemon_data(ability_id, url, session)
                                for ability_id in list_of_ids_or_names]
            responses = await asyncio.gather(*async_coroutines)
            pokemon_list = []
            for counter in range(len(responses)):
                pokemon_name = responses[counter].get("name")
                pokemon_id = responses[counter].get("id")
                height = responses[counter].get("height")
                weight = responses[counter].get("weight")
                types = [pokemon_type.get("type").get("name") for pokemon_type in responses[counter].get("types")]
                list_of_abilities_name = [ability.get("ability").get("name") for ability in
                                          responses[counter].get("abilities")]
                if self._expanded:
                    list_of_stats_names = [stat.get("stat").get("name") for stat in responses[counter].get("stats")]
                    stats_list = await StatRequestFactory.process_requests(list_of_stats_names)
                    abilities_list = await AbilityRequestFactory.process_requests(list_of_abilities_name)
                    list_of_moves_name = [move.get("move").get("name") for move in responses[counter].get("moves")]
                    moves_list = await MoveRequestFactory.process_requests(list_of_moves_name)
                    pokemon = Pokemon(pokemon_name, pokemon_id, height, weight,
                                      stats_list, types, abilities_list, moves_list)
                else:
                    stats = [(stat.get("stat").get("name"), stat.get("base_stat"))
                             for stat in responses[counter].get("stats")]
                    moves = [('Move name: %s' % (move.get("move").get("name")),
                              'Level acquired: %s' % (move.get("version_group_details")[0].get("level_learned_at")))
                             for move in responses[counter].get("moves")]
                    pokemon = Pokemon(pokemon_name, pokemon_id, height, weight,
                                      stats, types, list_of_abilities_name, moves)
                pokemon.expanded = self._expanded
                pokemon_list.append(pokemon)
            return pokemon_list
