# 30. Substring with Concatenation of All Words
# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words
# exactly once and without any intervening characters.
# Naive Algorithm
# 1. Construct a counter (template) mapping each word in words to the number of
#    times it appaers
# 2. Let num_words be the length of words. For each potential starting position
#    i, generate construct a counter of the num_words starting at i. Compare the
#    counters to see if they match. If they do, i is a solution.
# 3. Return a List containing all valid i's found in step 2.
from collections import Counter
from typing import Counter as CounterType
from typing import List

from utils import timing


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        num_words = len(words)
        word_length = len(words[0])
        template: CounterType[str] = Counter(words)
        return [
            i
            for i in range(len(s))
            if self.isValidStartingPosition(s, i, template, word_length, num_words)
        ]

    def isValidStartingPosition(
        self,
        s: str,
        i: int,
        template: CounterType[str],
        word_length: int,
        num_words: int,
    ) -> bool:
        total_length = num_words * word_length
        if i + total_length > len(s):
            # Not enough chars remaining
            return False
        counts: CounterType[str] = Counter()
        for n in range(num_words):
            word = s[i : i + word_length]
            if word not in template or counts[word] == template[word]:
                return False
            counts[word] += 1
            i += word_length
        return True


try:
    import pytest

    @pytest.mark.parametrize(
        ("s", "words", "expected"),
        [
            ("word", ["word"], [0]),
            ("bword", ["word"], [1]),
            ("birdword", ["bird", "word"], [0]),
            ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
            ("wordgoodgoodgoodbestword", ["good", "good"], [4, 8]),
        ],
    )
    def testFindSubstring(s: str, words: List[str], expected: List[str]) -> None:
        with timing(f"naive"):
            result = Solution().findSubstring(s, words)
        assert sorted(result) == sorted(expected)


except ModuleNotFoundError:
    pass
