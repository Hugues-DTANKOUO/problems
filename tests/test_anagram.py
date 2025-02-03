from time import sleep

import pytest

from problems.anagram import anagram
from problems.inside_test import anagram_test


def correct_anagram(word_1: str, word_2: str) -> bool:
    """
    Check if two words are anagrams of each other.

    :param word_1: The first word.
    :param word_2: The second word.
    :return: True if the words are anagrams, False otherwise
    """

    return sorted(word_1.lower()) == sorted(word_2.lower())


async def test_test_case_with_two_short_anagrams_and_base_function_then_error() -> None:
    """
    GIVEN a test case with two short anagrams and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The words are anagrams"):
        await anagram_test.anagram_with_two_short_anagrams_test(anagram)


async def test_test_case_with_two_short_anagrams_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with two short anagrams and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await anagram_test.anagram_with_two_short_anagrams_test(correct_anagram)


async def test_test_case_with_two_short_non_anagrams_and_base_function_then_error() -> None:
    """
    GIVEN a test case with two short non-anagrams and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The words are not anagrams"):
        await anagram_test.anagram_with_two_short_non_anagrams_test(anagram)


async def test_test_case_with_two_short_non_anagrams_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with two short non-anagrams and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await anagram_test.anagram_with_two_short_non_anagrams_test(correct_anagram)


async def test_test_case_with_two_long_anagrams_and_base_function_then_error() -> None:
    """
    GIVEN a test case with two long anagrams and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The words are anagrams"):
        await anagram_test.anagram_with_two_long_anagrams_test(anagram)


async def test_test_case_with_two_long_anagrams_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with two long anagrams and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await anagram_test.anagram_with_two_long_anagrams_test(correct_anagram)


async def test_test_case_with_two_long_non_anagrams_and_base_function_then_error() -> None:
    """
    GIVEN a test case with two long non-anagrams and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="The words are not anagrams"):
        await anagram_test.anagram_with_two_long_non_anagrams_test(anagram)


async def test_test_case_with_two_long_non_anagrams_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with two long non-anagrams and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await anagram_test.anagram_with_two_long_non_anagrams_test(correct_anagram)


async def test_test_case_with_two_long_anagrams_and_slow_correct_function_then_error() -> None:
    """
    GIVEN a test case with two long anagrams and slow correct function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """

    def slow_anagram(word_1: str, word_2: str) -> bool:
        """
        Check if two words are anagrams of each other.

        :param word_1: The first word.
        :param word_2: The second word.
        :return: True if the words are anagrams, False otherwise
        """
        sleep(1)
        return correct_anagram(word_1, word_2)

    with pytest.raises(AssertionError, match="Function timed out after 100 milliseconds"):
        await anagram_test.anagram_with_two_long_anagrams_test(slow_anagram)
