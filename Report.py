import datetime

from Request import Request
from pokeretriever.PokedexObject import PokedexObject


class Report:
    """
    Class representation of a Report.
    """
    def __init__(self, pokedex_object: PokedexObject):
        """
        Initializer for Report.
        :param pokedex_object: PokedexObject
        """
        self._report = Report.__format_report(pokedex_object)

    @staticmethod
    def __format_report(pokedex_object) -> str:
        """
        static method formats the report.
        :param pokedex_object: PokedexObject, list
        :return: str
        """
        formatted_report = f"Timestamp: {datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')}\n"
        if type(pokedex_object) is list:
            formatted_report += f"Number of requests: {len(pokedex_object)}\n"
            return formatted_report + "\n".join(map(lambda pokedex: pokedex.__str__(), pokedex_object))
        return formatted_report + pokedex_object.__str__()

    def print_a_report(self, user_request: Request):
        """
        Method prints the report.
        :param user_request: Request
        :return: void
        """
        if user_request.output == "print":
            print(self._report)
        else:
            with open(user_request.output, mode='a+', encoding='utf-8') as output_file:
                output_file.write(self._report)
