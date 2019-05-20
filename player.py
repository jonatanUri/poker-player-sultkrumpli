
class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):

        myStack = game_state["players"]["in_action"]["stack"]
        simpleRaise(game_state["current_buy_in"], game_state["players"]["in_action"]["bet"], game_state["minimum_raise"])

        return game_state["players"]["in_action"]["stack"]

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



cardValues = dict(
    J=11,
    Q=12,
    K=13,
    A=14
)
