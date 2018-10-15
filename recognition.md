
# What are the possibilities of an recognized pattern?




a) There is a single occurrence possible. For example bombs of one kind (quadruplets or single colored straights)

b) In the general case a pattern is usually not unique by itself. For example: tuple is also present if it is actually a triple,
   a straight can be longer than the needed length, a full house can be built with different tuples without even changing its height.

Now what is important to know in order to justify the probability?

## Protocol between Player and Server

* Should the player directly give a pattern or just a bunch of cards?
  The logic of recognizing patterns must be implemented anyways.

* Pro "Cards Only":

  * Simplicity of the protocol
  * The server needs to check the validity anyways
  
* Pro "Patterns":
  
  * Logic of Patterns is already available for AI logic
  * ?



## Complex Pattern Classes

The idea is to pack all cards that can be used by a pattern into one pattern
object and not multiple. For example looking for a pair in
> r4 g4 b4 

will return one pattern object that yields 3 possible pairs.
Or for example if we are looking for a straight there is one more parameter
since the length of a straight can vary:
> maj r2 r3 b4 b5 g6 r6 b7

will return a StraightPattern with 2 possibilities. Respectively there 
are more if including partial straights. Straits could also yield a split
info (build to independent straight).

In general a pattern object should yield the following info:
* Possible combinations for the pattern 
* Is it possible to beat another pattern?
* The cards potentially used by the pattern
* Which cards are of value for the resp. pattern. 
  For a straight a card that is available twice is of 
  less value than a one that occurs only once
* Should there be a class that collects all the patterns of one type?



