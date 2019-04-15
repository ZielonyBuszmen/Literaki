# plik z "helpersami"
import random

from backend.GamePlusMinus.catchwords import CATCHWORDS


def get_random_catchword():
    return random.choice(CATCHWORDS)


def get_catchword_mock(catchword):
    result = list()
    for index, letter in enumerate(catchword):
        new_letter = '_' if letter.isalpha() else letter
        result.append(new_letter)
    return ''.join(result)
