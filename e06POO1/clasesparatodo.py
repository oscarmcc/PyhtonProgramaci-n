class Menu:
    def __init__(self, *options):
        if len(options) == 1 and isinstance(options[0], (list, tuple)):
            self.options = list(options[0])

    def show_options(self, ):
        max_len_word = self.options[0]
        for n in range(1, len(self.options)):
            if len(max_len_word) < len(self.options[n]):
                max_len_word = self.options[n]
        for i in range(len(self.options)):
            print(f"{i + 1}.{self.options[i]}")
        print('-' * (len(max_len_word) + 3))
