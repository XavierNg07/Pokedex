How Pokedex works:
I used the Factory design pattern as well as the Facade design pattern for our implementation.
I made classes for each pokemon mode as well as an enum for that to get each mode from the api. I have a
Ability, Stat, Move, and Pokemon classes that all use factory classes to get the request. I put all these
classes in the pokeretriever package for the Facade implementation. Outside of this package I made a
Request class that contains all the data gathered from the setup_request_commandline in the pokedex.py module.
The base class is the PokedexObject which defines the informations for each pokemon.

Errors that are not handled/accounted for:
All errors have been handled, and all requirements have been implements.