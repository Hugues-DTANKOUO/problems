from pathlib import Path
from problems.anagram import is_anagram
from unittest import mock
from time import time
from typing import Callable

DATA_PATH = Path(__file__).parent / "data" / "anagram"


def _non_functional_check(func: Callable[[str, str], bool]) -> Callable[[str, str], bool]:
    """
    A decorator that checks if the function is_anagram is implemented correctly.

    The function should not use the sorted() function or implement its own sorting algorithm.
    The function should not take more than 0.01 seconds to execute

    :param func: The function to check
    :return: The wrapper function
    """

    def wrapper(word_1: str, word_2: str) -> bool:
        with mock.patch("problems.anagram.sorted", side_effect=sorted) as mock_sorted:
            start_time = time()
            result = func(word_1, word_2)
            duration = time() - start_time
            assert duration < 0.01, f"The function is too slow ({duration*1e3:.5f} milliseconds)"
            count_sorted = mock_sorted.call_count
            assert count_sorted == 0, f"sorted() was called {count_sorted} times, please do not use it"
            return result

    return wrapper


_is_anagram_without_sorted = _non_functional_check(is_anagram)


def test_is_anagram_with_two_short_anagrams() -> None:
    """
    GIVEN two short anagrams
    WHEN the function is_anagram is called
    THEN it should return True
    """
    # Load the words from the file
    with open(DATA_PATH / "good" / "word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "good" / "word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _is_anagram_without_sorted(word1, word2) is True


def test_is_anagram_with_two_short_non_anagrams() -> None:
    """
    GIVEN two short non-anagrams
    WHEN the function is_anagram is called
    THEN it should return False
    """
    # Load the words from the file
    with open(DATA_PATH / "bad" / "word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "bad" / "word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _is_anagram_without_sorted(word1, word2) is False


def test_is_anagram_with_two_long_anagrams() -> None:
    """
    GIVEN two long anagrams
    WHEN the function is_anagram is called
    THEN it should return True
    """
    # Load the words from the file
    with open(DATA_PATH / "good" / "long_word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "good" / "long_word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _is_anagram_without_sorted(word1, word2) is True


def test_is_anagram_with_two_long_non_anagrams() -> None:
    """
    GIVEN two long non-anagrams
    WHEN the function is_anagram is called
    THEN it should return False
    """
    # Load the words from the file
    with open(DATA_PATH / "good" / "long_word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "bad" / "word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    assert _is_anagram_without_sorted(word1, word2) is False
