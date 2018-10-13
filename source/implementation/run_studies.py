from tstudies import straights, bombs, doublestraight, fullhouse
from tlogic import generate_deck

deck=generate_deck();
print (straights.street_my_hand(deck))
print (straights.street_any_hand(deck))
print (straights.street_any_hand(deck, ph=True))
print (fullhouse.full_house_myhand(deck))
print (fullhouse.full_house_myhand(deck, ph=True))
bombs.bomb(deck)

