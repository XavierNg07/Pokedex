import abc


class PokedexObject(abc.ABC):
    """
    Abstract class representation of a blueprint for the PokedexObject.
    """
    @abc.abstractmethod
    def __init__(self, name: str, pokedex_id: int):
        """
        Initializer for PokedexObject.
        :param name: string
        :param pokedex_id: int
        """
        self._name = name
        self._id = pokedex_id

    @property
    def name(self):
        """
        Property for Pokemon name.
        :return: string
        """
        return self._name

    @property
    def id(self):
        """
        Property for Pokemon id.
        :return: int
        """
        return self._id

    @abc.abstractmethod
    def __str__(self):
        """
        String representation of a Pokemon object.
        :return: string
        """
        return f"----PokedexObject----\n" \
               f"Name: {self._name}\n" \
               f"Id: {self._id}"
