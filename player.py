
class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):

        myStack = game_state["players"]["in_action"]["stack"]
        simpleRaise(game_state["current_buy_in"], game_state["players"]["in_action"]["bet"], game_state["minimum_raise"])

        cardsInPlay = getCardsInPlay(game_state)
        cardsInHand = getCardsInHand(game_state)

        if cardsInHand[0]["rank"] == cardsInHand[1]["rank"]:
            return game_state["players"]["in_action"]["stack"]

        if cardsInHand[0]["suit"] == cardsInHand[1]["suit"]:
            return simpleRaise(game_state["current_buy_in"], game_state["players"]["in_action"]["bet"], game_state["minimum_raise"])

        return 0

    def showdown(self, game_state):
        pass


def simpleRaise(current_buy_in, bet, minimum_raise):
    return current_buy_in - bet + minimum_raise


def getCardsInPlay(game_state):
    hand = game_state["players"]["in_action"]["hole_cards"]
    table = game_state["community_cards"]
    all = []
    for card in hand:
        all.append(card)
    for card in table:
        all.append(card)
    return all

def getCardsInHand(game_state):
    return game_state["players"]["in_action"]["hole_cards"]

cardValues = dict(
    J=11,
    Q=12,
    K=13,
    A=14
)
