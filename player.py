
class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):

        return game_state["players"]["in_action"]["stack"]

    def showdown(self, game_state):
        pass



