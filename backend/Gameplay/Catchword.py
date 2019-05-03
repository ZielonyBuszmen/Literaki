from backend.Gameplay import game_helpers


class Catchword:
    def __init__(self):
        random_password = game_helpers.get_random_catchword()
        self.catchword = random_password['catchword']
        self.catchword_category = random_password['category']
        self.broke = game_helpers.get_catchword_mock(self.catchword)

    def get_broke(self) -> str:
        return self.broke

    def set_broke(self, broke) -> None:
        self.broke = broke

    def get_category(self) -> str:
        return self.catchword_category

    def is_correct_catchword(self, entered: str) -> bool:
        catchword = self.__alfabetize(self.catchword.lower())
        entered_catchword = self.__alfabetize(entered.lower())
        return catchword == entered_catchword

    def is_catchword_filled(self) -> bool:
        return self.catchword == self.broke

    def is_letter_in(self, letter: str) -> bool:
        return letter in self.catchword

    def fill_catchword(self, letter: str) -> None:
        index = 0
        for password_letter in self.catchword:
            if password_letter == letter:
                self.broke = self.broke[:index] + letter + self.broke[index + 1:]
            index += 1

    def __alfabetize(self, text):
        return ''.join(ch for ch in text if ch.isalnum())
