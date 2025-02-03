from pathlib import Path
from typing import Callable

from problems.inside_test.util import async_timeout


DATA_PATH = Path(__file__).parent / "data" / "anagram"


async def anagram_with_two_short_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two short anagrams
    WHEN the function anagram is called
    THEN it should return True
    """
    _functional_anagram = async_timeout(100)(func)

    # Check if the words are anagrams
    result: bool = await _functional_anagram("python", "yhonpt")
    assert result is True, "The words are anagrams"


async def anagram_with_two_short_non_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two short non-anagrams
    WHEN the function anagram is called
    THEN it should return False
    """
    _functional_anagram = async_timeout(100)(func)

    # Check if the words are anagrams
    result: bool = await _functional_anagram("abcdefghijklml", "xyzakjbkkafjak")
    assert result is False, "The words are not anagrams"

    result = await _functional_anagram("abcdefghijklml", "abcdefghijklmlz")
    assert result is False, "The words are not anagrams"

    result = await _functional_anagram("abcdefghijklml", "abcdefghijklm")
    assert result is False, "The words are not anagrams"


async def anagram_with_two_long_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two long anagrams
    WHEN the function anagram is called
    THEN it should return True
    """
    _functional_anagram = async_timeout(100)(func)
    # Load the words from the file
    with open(DATA_PATH / "long_word1.txt") as file1:
        word1 = file1.read().strip()
    with open(DATA_PATH / "long_word2.txt") as file2:
        word2 = file2.read().strip()

    # Check if the words are anagrams
    result: bool = await _functional_anagram(word1, word2)
    assert result is True, "The words are anagrams"


async def anagram_with_two_long_non_anagrams_test(func: Callable[[str, str], bool]) -> None:
    """
    GIVEN two long non-anagrams
    WHEN the function anagram is called
    THEN it should return False
    """
    _functional_anagram = async_timeout(100)(func)
    # Load the words from the file
    with open(DATA_PATH / "long_word1.txt") as file1:
        word1 = file1.read().strip()

    # Check if the words are anagrams
    result: bool = await _functional_anagram(word1, "xyzakjbkkafjak")
    assert result is False, "The words are not anagrams"
