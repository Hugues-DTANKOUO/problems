from typing import Callable

from problems.inside_test.util import async_timeout


async def palindrome_simple_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a simple string
    WHEN the palindrome function is called
    THEN it should return True for palindromes
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("kayak") is True, "kayak should be a palindrome"
    assert await _functional_palindrome("hello") is False, "hello should not be a palindrome"


async def palindrome_with_spaces_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a string with spaces
    WHEN the palindrome function is called
    THEN it should ignore spaces
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("never odd or even") is True, "never odd or even should be a palindrome"
    assert await _functional_palindrome("race a car") is False, "race a car should not be a palindrome"


async def palindrome_with_punctuation_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a string with punctuation
    WHEN the palindrome function is called
    THEN it should ignore punctuation
    """
    _functional_palindrome = async_timeout(100)(func)

    assert (
        await _functional_palindrome("A man, a plan, a canal: Panama!") is True
    ), "A man, a plan... should be a palindrome"
    assert await _functional_palindrome("race a car.") is False, "race a car should not be a palindrome"


async def palindrome_case_insensitive_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a string with mixed case
    WHEN the palindrome function is called
    THEN it should be case insensitive
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("Able was I ere I saw Elba") is True, "Able was I... should be a palindrome"
    assert await _functional_palindrome("Hello World") is False, "Hello World should not be a palindrome"


async def palindrome_with_numbers_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a string with numbers
    WHEN the palindrome function is called
    THEN it should treat numbers as characters
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("12321") is True, "12321 should be a palindrome"
    assert await _functional_palindrome("12345") is False, "12345 should not be a palindrome"


async def palindrome_with_empty_string_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN an empty string
    WHEN the palindrome function is called
    THEN it should return True
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("") is True, "An empty string should be a palindrome"


async def palindrome_with_single_character_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a single character
    WHEN the palindrome function is called
    THEN it should return True
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("a") is True, "a should be a palindrome"
    assert await _functional_palindrome("b") is True, "b should be a palindrome"


async def palindrome_with_long_string_test(func: Callable[[str], bool]) -> None:
    """
    GIVEN a long string
    WHEN the palindrome function is called
    THEN it should return True for palindromes
    """
    _functional_palindrome = async_timeout(100)(func)

    assert await _functional_palindrome("a" * 10000) is True, "a * 10000 should be a palindrome"
    assert await _functional_palindrome("ab" * 5000) is False, "ab * 5000 should not be a palindrome"
