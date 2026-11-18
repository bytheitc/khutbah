"""Find Qur'an quotations in transcripts and annotate them with exact Uthmani text."""

from functools import lru_cache

from khutbah.match import Matcher, Quotation

__all__ = [
    "Matcher",
    "Quotation",
    "find",
    "annotate",
]


@lru_cache(maxsize=1)
def _default_matcher() -> Matcher:
    return Matcher()


def find(
    text: str,
    *,
    min_words: int = 4,
    min_confidence: float = 0.6,
) -> list[Quotation]:
    """Find Qur'an quotations in ``text``."""
    if min_words == 4 and min_confidence == 0.6:
        return _default_matcher().find(text)
    return Matcher(min_words=min_words, min_confidence=min_confidence).find(text)


def annotate(
    text: str,
    *,
    min_words: int = 4,
    min_confidence: float = 0.6,
) -> str:
    """Replace recognized Qur'an quotations in ``text`` with exact Uthmani text and references."""
    if min_words == 4 and min_confidence == 0.6:
        return _default_matcher().annotate(text)
    return Matcher(min_words=min_words, min_confidence=min_confidence).annotate(text)
