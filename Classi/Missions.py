class Mission:

    def __init__(self, description, money_reward, difficulty, exp_reward):
        self.description = description
        self.money_reward = money_reward
        self.difficulty = difficulty
        self.exp_reward = exp_reward
        self.completed = False

    def print_description(self):
        """
        Stampa la descrizione della missione
        :return:
        """
        print(self.description)

    def print_status(self):
        """
        Stampa lo stato della missione
        :return:
        """
        print(self.completed)

    def update_status(self):
        """
        Aggiorna lo stato della missione
        :return:
        """
        self.completed = True

