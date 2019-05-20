
class Player:
    VERSION = "1.19"

    def betRequest(self, game_state):
        bet_size = 20

        try:
            AllIn = game_state["players"][game_state["in_action"]]["stack"]
            simpleRaise(game_state["current_buy_in"], game_state["players"][game_state["in_action"]]["bet"], game_state["minimum_raise"])

            cardsInPlay = getCardsInPlay(game_state)
            cardsInHand = getCardsInHand(game_state)

            minimum_raise = game_state["current_buy_in"] + game_state["minimum_raise"]
            if game_state["players"][game_state["in_action"]]["bet"] > bet_size:
                return 0

            # if isPreFlop(game_state):
            #     if cardsInHand[0]["rank"] > cardsInHand[1]["rank"]:
            #         if cardsInHand[0]["rank"] - cardsInHand[1]["rank"] > 3:
            #             return 0
            #     if cardsInHand[0]["rank"] < cardsInHand[1]["rank"]:
            #         if cardsInHand[1]["rank"] - cardsInHand[0]["rank"] > 3:
            #             return 0
            #
            # if cardsInHand[0]["rank"] == 7 and cardsInHand[1]["rank"] == 2:
            #     return 0
            # elif cardsInHand[0]["rank"] == 2 and cardsInHand[1]["rank"] == 7:
            #     return 0


            try:
                if game_state["current_buy_in"] < game_state["players"][game_state["in_action"]]["stack"]/20:
                    bet_size = game_state["current_buy_in"]/20
                if len(cardsInPlay) < 3:
                    if cardsInHand[0]["rank"] + cardsInHand[1]["rank"] > 18:
                        bet_size = minimum_raise
                    if cardsInHand[0]["rank"] + cardsInHand[1]["rank"] > 20:
                        bet_size += minimum_raise
                    if cardsInHand[0]["suit"] == cardsInHand[1]["suit"]:
                        # bet_size = bet_size
                        pass
                    if countPairs(game_state) == 1:
                        bet_size += game_state["players"][game_state["in_action"]]["stack"]/8
                    if cardsInHand[0]["rank"] == cardsInHand[1]["rank"]:
                        bet_size += minimum_raise
            except:
                print("---error3")

            if isStraight(cardsInPlay):
                bet_size = AllIn

            if countPairs(game_state) >= 2:
                bet_size = AllIn

            if cardsInHand[0]["rank"] < 9 or cardsInHand[1]["rank"] < 9 and game_state["current_buy_in"] > game_state["players"][game_state["in_action"]]["stack"]/2 and countPairs(game_state)<2 and not isFlush(game_state) and not isStraight(cardsInPlay):
                return 0
            elif countPairs(game_state)>2 and isFlush(game_state) and isStraight(cardsInPlay):
                return game_state["players"][game_state["in_action"]]["stack"]/2

        finally:
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
    for card in table:
        if cardsInHand[0]["rank"] == card["rank"] or cardsInHand[1]["rank"] == card["rank"]:
            pairs += 1
    return pairs


def isFlush(game_state):
    all_cards = getCardsInPlay(game_state)
    first_card_suit = all_cards[0]["suit"]
    flush = []
    for card in all_cards:
        if card["suit"] == first_card_suit:
            flush.append(card["suit"])
    if len(flush) == 3:
        return "chance for flush"
    elif len(flush) == 4:
        return "greater chance for flush"
    elif len(flush) == 5:
        return True
    else:
        return False


def isStraight(cards_in_play):
    hand = cards_in_play[0:2]
    table = cards_in_play[1:]
    reverse_cards = cards_in_play
    reverse_cards.sort(reverse=True)
    cards_in_play.sort()

    count = 0
    for i, card in enumerate(cards_in_play):
        if i+1 > len(cards_in_play):
            break
        if card["rank"] < cards_in_play[i+1]["rank"] and card["rank"]-cards_in_play[i+1]["rank"] == -1:
            count += 1
            continue
        if i == 4 or count == 4:
            if hand[0]["rank"] in cards_in_play["rank"] or hand[1]["rank"] in cards_in_play["rank"]:
                return True
    count = 0
    for i, card in enumerate(reverse_cards):
        if i+1 > len(cards_in_play):
            break
        if card["rank"] > cards_in_play[i+1]["rank"] and card["rank"]-cards_in_play[i+1]["rank"] == 1:
            count += 1
            continue
        if i == 4 or count == 4:
            if hand[0]["rank"] in cards_in_play["rank"] or hand[1]["rank"] in cards_in_play["rank"]:
                return True

    return False


def isPreFlop(game_state):
    if len(convertCards(game_state["community_cards"])) == 0:
        return True
    return False


def isPairInHand(cardsInHand):
    if cardsInHand[0]["rank"] == cardsInHand[1]["rank"]:
        return True
    return False


