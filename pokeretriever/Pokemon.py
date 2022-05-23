from pokeretriever.PokedexObject import PokedexObject


class Pokemon(PokedexObject):
    """
    Class representation of Pokemon which inherits from PokedexObject.
    """
    def __init__(self, pokemon_name: str, pokemon_id: int, height: int, weight: int,
                 stats: list, pokemon_types: list, abilities: list, moves: list):
        """
        Initializer for Pokemon.
        :param pokemon_name: str
        :param pokemon_id: int
        :param height: int
        :param weight: int
        :param stats: list
        :param pokemon_types: list
        :param abilities: list
        :param moves: list
        """
        super().__init__(pokemon_name, pokemon_id)
        self._height = height
        self._weight = weight
        self._stats_list = stats
        self._types = pokemon_types
        self._abilities_list = abilities
        self._moves_list = moves
        self._expanded = False

    @property
    def expanded(self):
        """
        Property for expanded.
        :return: bool
        """
        return self._expanded

    @expanded.setter
    def expanded(self, value):
        """
        Getter for expanded.
        :param value: bool
        :return: void
        """
        self._expanded = value

    def _format_expanded_stats(self) -> str:
        """
        Method formats the stats data.
        :return: string
        """
        formatted_output = "Stats:\n------\n"
        for stat in self._stats_list:
            formatted_output += f"{stat.__str__()}\n\n"
        return formatted_output

    def _format_expanded_abilities(self) -> str:
        """
        Method  formats the abilities data.
        :return: string
        """
        formatted_output = "Abilities:\n------\n"
        for ability in self._abilities_list:
            formatted_output += f"{ability.__str__()}\n\n"
        return formatted_output

    def _format_expanded_moves(self) -> str:
        """
        Method formats the moves data.
        :return: string
        """
        formatted_output = "Moves:\n------\n"
        for move in self._moves_list:
            formatted_output += f"{move.__str__()}\n\n"
        return formatted_output

    def _format_default_stats(self) -> str:
        """
        Method formats the defaults stats data.
        :return: string
        """
        formatted_output = "Stats:\n------\n"
        for stat in self._stats_list:
            formatted_output += f"{stat}\n"
        return formatted_output

    def _format_default_abilities(self) -> str:
        """
        Method formats defaults abilities data.
        :return: string
        """
        formatted_output = "Abilities:\n------\n"
        for ability in self._abilities_list:
            formatted_output += f"{ability}\n"
        return formatted_output

    def _format_default_moves(self) -> str:
        """
        Method formats default moves data.
        :return: string
        """
        formatted_output = "Moves:\n------\n"
        for move in self._moves_list:
            formatted_output += f"{move}\n"
        return formatted_output

    def _format_types(self) -> str:
        """
        Method formats the pokemon types.
        :return: string
        """
        return ", ".join(self._types)

    def __str__(self):
        """
        String representation of class.
        :return: string
        """
        output = f'Name: {self.name}' \
                 f'\nID: {self.id}' \
                 f'\nHeight: {self._height}' \
                 f'\nWeight: {self._weight}' \
                 f'\nTypes: {self._format_types()}'
        if self._expanded:
            output += f'\n{self._format_expanded_stats()}' \
                      f'\n{self._format_expanded_abilities()}'\
                      f'\n{self._format_expanded_moves()}'
        else:
            output += f'\n{self._format_default_stats()}' \
                      f'\n{self._format_default_abilities()}' \
                      f'\n{self._format_default_moves()}'
        return output
