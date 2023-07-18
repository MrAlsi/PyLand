class Mission:

    def __init__(self, description, status, money_reward, exp_reward):
        self.description = description
        self.status = status
        self.money_reward = money_reward
        self.exp_reward = exp_reward

    def print_description(self):
        print(self.description)

    def print_status(self):
        print(self.status)

    def update_status(self):
        # Implementa una funzione per fare aggiornare lo status
        pass

