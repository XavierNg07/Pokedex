from pokeretriever.PokedexObject import PokedexObject


class Stat(PokedexObject):
    """
    Class representation of the Pokemon's stats.
    """
    def __init__(self, stat_name: str, stat_id: int, is_battle_only: bool):
        """
        Initializer for Stats.
        :param stat_name: str
        :param stat_id: int
        :param is_battle_only: bool
        """
        super().__init__(stat_name, stat_id)
        self._is_battle_only = is_battle_only

    def __str__(self):
        """
        String representation os stat class.
        :return:
        """
        return f'Name: {self.name}' \
               f'\nID: {self.id}' \
               f'\nIs_Battle_Only: {self._is_battle_only}'
