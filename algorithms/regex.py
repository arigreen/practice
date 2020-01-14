from typing import Dict
from typing import Tuple

import pytest


def match_regex_with_cache(
    regex: str, candidate: str, cache: Dict[Tuple[str, str], bool] = None
) -> bool:
    if not cache:
        cache = {}
    if (regex, candidate) in cache:
        return cache[(regex, candidate)]

    if regex and regex[0] in ["?", "*"]:
        raise Exception("Malformed Regex")

    if len(regex) <= 1:
        result = regex == candidate
        cache[(regex, candidate)] = result
        return result

    # regex is at least 2 characters
    first_match = candidate and regex[0] == candidate[0]

    if regex[1] == "?":
        if first_match:
            result_using_match = match_regex_with_cache(regex[2:], candidate[1:], cache)
            cache[(regex[2:], candidate[1:])] = result_using_match
            if result_using_match:
                return True
        result_skipping_first_char = match_regex_with_cache(regex[2:], candidate, cache)
        cache[(regex[2:], candidate)] = result_skipping_first_char
        return result_skipping_first_char

    elif regex[1] == "*":
        if first_match:
            result_using_match = match_regex_with_cache(regex[2:], candidate[1:], cache)
            cache[(regex[2:], candidate[1:])] = result_using_match
            if result_using_match:
                return True
            # Keep using it
            result_skipping_first_char = match_regex_with_cache(
                regex, candidate[1:], cache
            )
            cache[(regex, candidate[1:])] = result_skipping_first_char
            return result_skipping_first_char
        else:
            cache[(regex, candidate)] = False
            return False

        if candidate[0] == regex[0]:
            result = match_regex_with_cache(regex[2:], candidate[1:], cache)
            cache[(regex[2:], candidate)] = result
            if result:
                return result
            else:
                result = match_regex_with_cache(regex, candidate[1:], cache)
                cache[(regex[2:], candidate)] = result
                return result

    else:
        # Normal character
        if first_match:
            result = match_regex_with_cache(regex[1:], candidate[1:], cache)
            cache[(regex[1:], candidate[1:])] = result
            return result
        else:
            cache[(regex, candidate)] = False
            return False


def match_regex(regex: str, candidate: str) -> bool:
    if len(regex) == 0:
        return regex == candidate

    if regex[0] == "?":
        raise Exception("Malformed Regex")

    if len(regex) == 1:
        return regex == candidate

    # regex is at least 2 characters
    if regex[1] == "?":
        if len(candidate) > 0 and regex[0] == candidate[0]:
            return match_regex(regex[2:], candidate) or match_regex(
                regex[2:], candidate[1:]
            )
        else:
            return match_regex(regex[2:], candidate)

    if len(candidate) > 0 and regex[0] == candidate[0]:
        return match_regex(regex[1:], candidate)

    return False


@pytest.mark.parametrize(
    "regex, input_s,expected",
    [
        ("a", "a", True),
        ("a", "b", False),
        ("a", "", False),
        ("", "a", False),
        ("a?", "a", True),
        ("a?", "", True),
        ("a?", "aa", False),
        ("a?", "b", False),
        (
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            False,
        ),
        (
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            True,
        ),
        ("a*", "a", True),
        ("a*", "aa", True),
        ("a*", "aab", False),
        ("a*b", "aab", True),
        (
            "aaaaaa*a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a?"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            True,
        ),
    ],
)
def test_regex(regex: str, input_s: str, expected: bool) -> None:
    assert match_regex_with_cache(regex, input_s, None) == expected
