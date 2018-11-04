"""
This is python, hence a few conventions (that are not really enforced, since we're all grown ups)

Patterns
========

Every Pattern has a __init__ with exactly the cards as a positional argument.
An instance of TPattern (e.g. TStraight) must be valid, otherways it must
raise a ValueException at creation (__init__)
The properties and methods are defined in TPattern (Abstract Class)
The properties can be implemented in two ways:
* as a method with a @propery annotation
* directly by defining a variable in __init__

The find function returns a list of all possible beating Pattern
ordered by the rank.
"""