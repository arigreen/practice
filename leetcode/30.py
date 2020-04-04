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
import itertools
from collections import Counter
from typing import Counter as CounterType
from typing import List

from utils import timing


class Solution:
    def findSubstringNaive(self, s: str, words: List[str]) -> List[int]:
        # For each position in S, check to see if the starting position is value
        # Worst case run time: O(s * n) where s is length of string and n is num
        # words
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

    def findSubstringOnePass(self, s: str, words: List[str]) -> List[int]:
        # O(s / word_length) *

        def get_stripe_results(i: int) -> List[int]:
            results = []
            counts: CounterType[str] = Counter()
            start = i
            end = i
            while end + word_length <= len(s):
                word = s[end : end + word_length]
                end += word_length
                if word not in template:
                    start = end
                    counts.clear()
                else:
                    counts[word] += 1
                    if counts[word] > template[word]:
                        # pop off from the beginning
                        while True:
                            current_word = s[start : start + word_length]
                            counts[current_word] -= 1
                            start += word_length
                            if current_word == word:
                                break
                if end - start == total_length:
                    results.append(start)
            return results

        if not words:
            return []
        num_words = len(words)
        word_length = len(words[0])
        total_length = num_words * word_length
        template: CounterType[str] = Counter(words)
        results_lists = [get_stripe_results(i) for i in range(word_length)]
        return list(itertools.chain(*results_lists))

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return self.findSubstringOnePass(s, words)


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
            ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ],
    )
    def testFindSubstring(s: str, words: List[str], expected: List[str]) -> None:
        with timing(f"naive"):
            result = Solution().findSubstringNaive(s, words)
        with timing(f"onepass"):
            result = Solution().findSubstringOnePass(s, words)
        assert sorted(result) == sorted(expected)


except ModuleNotFoundError:
    pass
