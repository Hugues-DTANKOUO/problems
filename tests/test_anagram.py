from problems.anagram import anagram
from problems.inside_test import anagram_test


def test_anagram_with_two_short_anagrams() -> None:
    """
    GIVEN two short anagrams
    WHEN the function anagram is called
    THEN it should return True
    """
    anagram_test.anagram_with_two_short_anagrams_test(anagram)


def test_anagram_with_two_short_non_anagrams() -> None:
    """
    GIVEN two short non-anagrams
    WHEN the function anagram is called
    THEN it should return False
    """
    anagram_test.anagram_with_two_short_non_anagrams_test(anagram)


def test_anagram_with_two_long_anagrams() -> None:
    """
    GIVEN two long anagrams
    WHEN the function anagram is called
    THEN it should return True
    """
    anagram_test.anagram_with_two_long_anagrams_test(anagram)


def test_anagram_with_two_long_non_anagrams() -> None:
    """
    GIVEN two long non-anagrams
    WHEN the function anagram is called
    THEN it should return False
    """
    anagram_test.anagram_with_two_long_non_anagrams_test(anagram)
