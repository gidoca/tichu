from tstudies import straights, bombs
from tlogic import generate_deck

deck=generate_deck();
straights.street_my_hand(deck)
straights.street_any_hand(deck)
straights.street_any_hand(deck, ph=True)
bombs.bomb(deck)
