
class Player:
    VERSION = "1.13"

    def betRequest(self, game_state):

        AllIn = game_state["players"][game_state["in_action"]]["stack"]
        simpleRaise(game_state["current_buy_in"], game_state["players"][game_state["in_action"]]["bet"], game_state["minimum_raise"])

        cardsInPlay = getCardsInPlay(game_state)
        cardsInHand = getCardsInHand(game_state)

        bet_size = 10
        minimum_raise = game_state["current_buy_in"] + game_state["minimum_raise"]

        if cardsInHand[0]["rank"] == 7 and cardsInHand[1]["rank"] == 2:
            return 0
        elif cardsInHand[0]["rank"] == 2 and cardsInHand[1]["rank"] == 7:
            return 0

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

        if countPairs(game_state) >= 3:
                bet_size = AllIn

        return bet_size

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
    cards = game_state["players"][game_state["in_action"]]["hole_cards"]
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

def pairOnTable(game_state):
    table = convertCards(game_state["community_cards"])
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i]["rank"] == table[j]["rank"] and i != j:
                return table[i]["rank"]
    return None

def countPairs(game_state):
    pairs = 0
    table = convertCards(game_state["community_cards"])
    cardsInHand = getCardsInHand(game_state)
    for i in range(len(table)):
        if cardsInHand[0]["rank"] == table[i]["rank"] or cardsInHand[1]["rank"] == table[i]["rank"]:
            pairs += 1
    return pairs
