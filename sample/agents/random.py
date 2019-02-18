
import random
from agents.base import BaseAgent

class RandomAgent(BaseAgent):

    def __init__(self, actions, stocks):
        self._log("Initialized")
        super(RandomAgent, self).__init__(actions, stocks)
        self._log("Cash: {0:.2f}".format(self.get_cash()))
        self._log("Profit: {0:.2f}".format(self.get_profit()))

    def _log_cash(self):
        self._log("Cash: {0:.2f}".format(self.get_cash()))

    def log_action(self, act):
        act = act.capitalize()
        act = act + "ing"
        self._log(act)
        # if act is 'sell' or 'buy':
        #     self.log_cash()

    def act(self, action_price):
        infos = self.request_notifications()
        selected_actions = []
        temp_cash = self.cash
        for stock, info in infos:
            actions = self.actions[:]
            if temp_cash < action_price:
                actions.remove('buy')
            if stock.wallet_size() == 0:
                actions.remove('sell')
            actions_size = len(actions)
            index = random.randrange(actions_size)
            action = actions[index]
            if action == 'buy':
                temp_cash -= action_price
            self.log_action("{}: {}".format(stock.get_name(), action))
            selected_actions.append((stock, action))
        return selected_actions

    @classmethod
    def _log(cls, msg):
        print("[RandomAgent] {}".format(msg))
