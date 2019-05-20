
class Player:
    VERSION = "1.9"

    def betRequest(self, game_state):
        try:
            AllIn = game_state["players"]["in_action"]["stack"]
            simpleRaise(game_state["current_buy_in"], game_state["players"]["in_action"]["bet"], game_state["minimum_raise"])

            cardsInPlay = getCardsInPlay(game_state)
            cardsInHand = getCardsInHand(game_state)
        except:
            print("---error1")

        bet_size = 10
        minimum_raise = game_state["current_buy_in"] + game_state["minimum_raise"]

        try:
            if cardsInHand[0]["rank"] == 7 and cardsInHand[1]["rank"] == 2:
                return 0
            elif cardsInHand[0]["rank"] == 2 and cardsInHand[1]["rank"] == 7:
                return 0
        except:
            print("---error2")

        try:
            if cardsInHand[0]["rank"] + cardsInHand[1]["rank"] > 18:
                bet_size = minimum_raise
            if cardsInHand[0]["rank"] + cardsInHand[1]["rank"] > 20:
                bet_size += minimum_raise
            if cardsInHand[0]["suit"] == cardsInHand[1]["suit"]:
                # bet_size = bet_size
                pass

            if cardsInHand[0]["rank"] == cardsInHand[1]["rank"]:
                bet_size += minimum_raise
        except:
            print("---error3")

        return game_state["current_buy_in"] - game_state["players"]["in_action"]["bet"]

    def showdown(self, game_state):
        pass


def simpleRaise(current_buy_in, bet, minimum_raise):
    return current_buy_in - bet + minimum_raise


def getCardsInPlay(game_state):
    hand = getCardsInHand(game_state)
    table = convertCards(game_state["community_cards"])

    all = []
    for card in hand:
        all.append(card)
    for card in table:
        all.append(card)

    return all


def getCardsInHand(game_state):
    cards = game_state["players"]["in_action"]["hole_cards"]
    return convertCards(cards)

cardValues = dict(
    J=11,
    Q=12,
    K=13,
    A=14
)


def convertCards(cards):
    for card in cards:
        if card["rank"] == "J":
            card["rank"] = 11
        elif card["rank"] == "Q":
            card["rank"] = 12
        elif card["rank"] == "K":
            card["rank"] = 13
        elif card["rank"] == "A":
            card["rank"] = 14
        else:
            card["rank"] = int(card["rank"])
    return cards

