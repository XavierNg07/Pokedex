from pokeretriever.PokedexObject import PokedexObject


class Move(PokedexObject):
    """
    Class representation of the Pokemon moves, which inherits from PokedexObject.
    """
    def __init__(self, move_name: str, move_id: int, generation: str,
                 accuracy: int, pp: int, power: int,
                 move_type: str, damage_class: str, short_effect: str):
        """
        Initializer for the Pokemon's moves.
        :param move_name: str
        :param move_id: int
        :param generation: str
        :param accuracy: int
        :param pp: int
        :param power: int
        :param move_type: str
        :param damage_class: str
        :param short_effect: str
        """
        super().__init__(move_name, move_id)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = move_type
        self._damage_class = damage_class
        self._short_effect = short_effect

    def __str__(self):
        """
        String representation of the Pokemon's moves.
        :return: string
        """
        return f'Name: {self.name}' \
               f'\nID: {self.id}' \
               f'\nGeneration: {self._generation}' \
               f'\nAccuracy: {self._accuracy}' \
               f'\nPP: {self._pp}' \
               f'\nPower: {self._power}' \
               f'\nType: {self._type}' \
               f'\nDamage Class: {self._damage_class}' \
               f'\nEffect (Short): {self._short_effect}'
