from pokeretriever.PokedexObject import PokedexObject


class Ability(PokedexObject):
    """
    Class representation of Ability of a Pokemon, which inherits from PokedexObject
    """
    def __init__(self, ability_name: str, ability_id: int, generation: str,
                 effect: str, short_effect: str, pokemon_list: list):
        """
        Initializer for Ability of a Pokemon.
        :param ability_name: string
        :param ability_id: int
        :param generation: string
        :param effect: str
        :param short_effect: str
        :param pokemon_list: list
        """
        super().__init__(ability_name, ability_id)
        self._generation = generation
        self._effect = effect
        self._short_effect = short_effect
        self._pokemon_list = pokemon_list

    def __str__(self):
        """
        String representation of Pokemon Abilities.
        :return: string
        """
        result = f'Name: {self.name}' \
                 f'\nID: {self.id}' \
                 f'\nGeneration: {self._generation}' \
                 f'\nEffect: {self._effect}' \
                 f'\nEffect (Short): {self._short_effect}' \
                 f'\nPokemon: '
        result += ", ".join(self._pokemon_list)
        return result
