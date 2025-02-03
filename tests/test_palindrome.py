from time import sleep

import pytest

from problems.inside_test import palindrome_test
from problems.palindrome import palindrome


def correct_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.

    :param text: String to check
    :return: True if the string is a palindrome, False otherwise
    """
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]


async def test_test_case_with_simple_palindrome_and_base_function_then_error() -> None:
    """
    GIVEN a test case with simple palindrome and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="kayak should be a palindrome"):
        await palindrome_test.palindrome_simple_test(palindrome)


async def test_test_case_with_simple_palindrome_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with simple palindrome and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_simple_test(correct_palindrome)


async def test_test_case_with_spaces_and_base_function_then_error() -> None:
    """
    GIVEN a test case with spaces and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="never odd or even should be a palindrome"):
        await palindrome_test.palindrome_with_spaces_test(palindrome)


async def test_test_case_with_spaces_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with spaces and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_with_spaces_test(correct_palindrome)


async def test_test_case_with_punctuation_and_base_function_then_error() -> None:
    """
    GIVEN a test case with punctuation and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="A man, a plan... should be a palindrome"):
        await palindrome_test.palindrome_with_punctuation_test(palindrome)


async def test_test_case_with_punctuation_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with punctuation and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_with_punctuation_test(correct_palindrome)


async def test_test_case_with_mixed_case_and_base_function_then_error() -> None:
    """
    GIVEN a test case with mixed case and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="Able was I... should be a palindrome"):
        await palindrome_test.palindrome_case_insensitive_test(palindrome)


async def test_test_case_with_mixed_case_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with mixed case and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_case_insensitive_test(correct_palindrome)


async def test_test_case_with_numbers_and_base_function_then_error() -> None:
    """
    GIVEN a test case with numbers and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="12321 should be a palindrome"):
        await palindrome_test.palindrome_with_numbers_test(palindrome)


async def test_test_case_with_numbers_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with numbers and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_with_numbers_test(correct_palindrome)


async def test_test_case_with_empty_string_and_base_function_then_error() -> None:
    """
    GIVEN a test case with empty string and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="An empty string should be a palindrome"):
        await palindrome_test.palindrome_with_empty_string_test(palindrome)


async def test_test_case_with_empty_string_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with empty string and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_with_empty_string_test(correct_palindrome)


async def test_test_case_with_single_char_and_base_function_then_error() -> None:
    """
    GIVEN a test case with single character and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match="a should be a palindrome"):
        await palindrome_test.palindrome_with_single_character_test(palindrome)


async def test_test_case_with_single_char_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with single character and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_with_single_character_test(correct_palindrome)


async def test_test_case_with_long_string_and_base_function_then_error() -> None:
    """
    GIVEN a test case with long string and base function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """
    with pytest.raises(AssertionError, match=r"a \* 10000 should be a palindrome"):
        await palindrome_test.palindrome_with_long_string_test(palindrome)


async def test_test_case_with_long_string_and_correct_function_then_success() -> None:
    """
    GIVEN a test case with long string and correct function
    WHEN the test case is run
    THEN any error should not be raised
    """
    await palindrome_test.palindrome_with_long_string_test(correct_palindrome)


async def test_test_case_with_palindrome_and_slow_correct_function_then_error() -> None:
    """
    GIVEN a test case with palindrome and slow correct function
    WHEN the test case is run
    THEN an AssertionError should be raised
    """

    def slow_palindrome(text: str) -> bool:
        """
        Check if a string is a palindrome with artificial delay.

        :param text: String to check
        :return: True if the string is a palindrome, False otherwise
        """
        sleep(1)
        return correct_palindrome(text)

    with pytest.raises(AssertionError, match="Function timed out after 100 milliseconds"):
        await palindrome_test.palindrome_simple_test(slow_palindrome)
