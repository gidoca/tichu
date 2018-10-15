from pychu.tlogic.thelpers import generate_deck
from pychu.tstudies import fullhouse
from pychu.tstudies import straights, bombs

deck=generate_deck();
print (straights.street_my_hand(deck))
print (straights.street_any_hand(deck))
print (straights.street_any_hand(deck, ph=True))
print (fullhouse.full_house_myhand(deck))
print (fullhouse.full_house_myhand(deck, ph=True))
bombs.bomb(deck)

