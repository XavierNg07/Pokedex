import argparse
import asyncio
from pathlib import Path
from PokedexMode import PokedexMode
from Report import Report
from Request import Request
from pokeretriever.AbilityRequestFactory import AbilityRequestFactory
from pokeretriever.MoveRequestFactory import MoveRequestFactory
from pokeretriever.PokedexObject import PokedexObject
from pokeretriever.PokemonRequestFactory import PokemonRequestFactory

"""
This module is the driver of our program.
Author: Xavier Nguyen
"""


def setup_request_commandline() -> Request:
    """
    Method sets up the request in the commandline.
    :return: Request
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("pokedex_mode", choices=["pokemon", "ability", "move"],
                        help="This argument specified the mode that the application will be opened in."
                             " In the pokemon mode, the input will be an id or the name of a pokemon."
                             " In the ability mode, the input will be an id or the name of a ability."
                             " These are certain effects that pokemon can enable."
                             " In the move mode, the input will be an id or the name of a pokemon move."
                             " These are the attacks and actions pokemon can take."
                             " The pokedex will query pokemon information.")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--inputfile", help="The text file including names (and/or) ids"
                                                 " of Pokemon/Ability/Move to be queried.")
    input_group.add_argument("--inputdata", help="A name or id of Pokemon/Ability/Move to be queried.")
    parser.add_argument("--expanded", action="store_true", default=False,
                        help="When this flag is provided,"
                             " certain attributes are expanded,"
                             "that is the pokedex will do "
                             "sub-queries to get more "
                             " information about a particular attribute."
                             " If this flag is not provided, the app will not get the"
                             " extra information and just print what's provided.")
    parser.add_argument("--output", default="print", help="If provided, a filename (with a .txt extension) must also"
                                                          " be provided. and the query result should be printed"
                                                          " to the specified text file. If this flag is not provided,"
                                                          " then print the result to the console")
    try:
        args = parser.parse_args()
        user_request = Request()
        user_request.mode = PokedexMode(args.pokedex_mode)
        user_request.data_input = args.inputdata
        user_request.input_file = args.inputfile
        user_request.expanded = args.expanded
        user_request.output = args.output
        return user_request
    except Exception as exception:
        print(f"Error! Could not read arguments.\n{exception}")
        quit()


class Pokedex:
    """
    Class representation of Pokedex
    """
    def __init__(self):
        """
        Initializer for a Pokedex
        """
        self._factory = None

    def _handle_request(self, user_request: Request) -> PokedexObject:
        """
        Method handles the request.
        :param user_request: Request
        :return: list, PokedexObject
        """
        loop = asyncio.get_event_loop()
        if user_request.input_file:
            if not Path(user_request.input_file).is_file():
                raise FileNotFoundError(f"No such file for reading: '{user_request.input_file}'")
            else:
                data_input = []
                with open(user_request.input_file, mode='r', encoding='utf-8') as user_file:
                    for line in user_file:
                        data_input.append(line.strip())
                return loop.run_until_complete(self._factory.process_requests(data_input))
        return loop.run_until_complete(self._factory.process_single_request(user_request.data_input))

    def execute_request(self, user_request: Request) -> PokedexObject:
        """
        Method executes the request.
        :param user_request: Request
        :return: list, PokedexObject
        """
        if user_request.mode == PokedexMode.POKEMON:
            self._factory = PokemonRequestFactory(user_request.expanded)
        elif user_request.mode == PokedexMode.ABILITY:
            self._factory = AbilityRequestFactory()
        else:
            self._factory = MoveRequestFactory()
        try:
            pokedex_object = self._handle_request(user_request)
        except FileNotFoundError as exception:
            print(f"File Not Found Exception caught! Exception: {exception}")
        else:
            return pokedex_object


def main(user_request: Request):
    pokedex = Pokedex()
    pokedex_object = pokedex.execute_request(user_request)
    report = Report(pokedex_object)
    report.print_a_report(user_request)


if __name__ == "__main__":
    request = setup_request_commandline()
    main(request)
