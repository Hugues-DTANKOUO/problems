from pathlib import Path
from time import time
from typing import Callable
from unittest import mock


DATA_PATH = Path(__file__).parent / "data" / "anagram"


def _non_functional_check(func: Callable[[str, str], bool]) -> Callable[[str, str], bool]:
    """
    A decorator that checks if the function anagram is implemented correctly.

    The function should not use the sorted() function or implement its own sorting algorithm.
    The function should not take more than 0.1 seconds to execute

    :param func: The function to check
    :return: The wrapper function
    """

    def wrapper(word_1: str, word_2: str) -> bool:
        with mock.patch("problems.anagram.sorted", side_effect=sorted) as mock_sorted:
            start_time = time()
            result = func(word_1, word_2)
            duration = time() - start_time
            assert duration < 0.1, f"The function is too slow ({duration*1e3:.5f} milliseconds)"
            count_sorted = mock_sorted.call_count
            assert count_sorted == 0, f"sorted() was called {count_sorted} times, please do not use it"
            return result

    return wrapper


def anagram_with_two_short_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two short anagrams
    WHEN the function anagram is called
    THEN it should return True
    """
    _anagram_without_sorted = _non_functional_check(func)
    # Load the words from the file
    with open(DATA_PATH / "good" / "word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "good" / "word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _anagram_without_sorted(word1, word2) is True, "The words are anagrams"


def anagram_with_two_short_non_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two short non-anagrams
    WHEN the function anagram is called
    THEN it should return False
    """
    _anagram_without_sorted = _non_functional_check(func)
    # Load the words from the file
    with open(DATA_PATH / "bad" / "word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "bad" / "word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _anagram_without_sorted(word1, word2) is False, "The words are not anagrams"


def anagram_with_two_long_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two long anagrams
    WHEN the function anagram is called
    THEN it should return True
    """
    _anagram_without_sorted = _non_functional_check(func)
    # Load the words from the file
    with open(DATA_PATH / "good" / "long_word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "good" / "long_word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _anagram_without_sorted(word1, word2) is True, "The words are anagrams"


def anagram_with_two_long_non_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two long non-anagrams
    WHEN the function anagram is called
    THEN it should return False
    """
    _anagram_without_sorted = _non_functional_check(func)
    # Load the words from the file
    with open(DATA_PATH / "good" / "long_word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "bad" / "word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _anagram_without_sorted(word1, word2) is False, "The words are not anagrams"
