# plik z "helpersami"
import random

from backend.Gameplay.catchword_list import CATCHWORDS


def get_random_catchword() -> dict:
    return random.choice(CATCHWORDS)


def get_catchword_mock(catchword: str) -> str:
    result = list()
    for index, letter in enumerate(catchword):
        new_letter = '_' if letter.isalpha() else letter
        result.append(new_letter)
    return ''.join(result)
