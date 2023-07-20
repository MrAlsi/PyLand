class Mission:

    def __init__(self, description, money_reward, difficulty, exp_reward):
        self.description = description
        self.money_reward = money_reward
        self.difficulty = difficulty
        self.exp_reward = exp_reward
        self.completed = False

    def print_description(self):
        print(self.description)

    def print_status(self):
        print(self.completed)

    def update_status(self):
        # Implementa una funzione per fare aggiornare lo status
        self.completed = True

