"""Interval ratios and tuning systems, for the Junior Music track.

Boethius's *On Music*, Zuckerkandl's *The Sense of Music*, and Kalkavage's
*On the Measurement of Tones* all turn on the question: what ratios of
string-length (or frequency) produce what perceived intervals? This module
provides just-intonation ratios, the Pythagorean comma, and a comparison
with equal temperament.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

JUST_RATIOS: dict[str, Fraction] = {
    "unison": Fraction(1, 1),
    "minor_second": Fraction(16, 15),
    "major_second": Fraction(9, 8),
    "minor_third": Fraction(6, 5),
    "major_third": Fraction(5, 4),
    "perfect_fourth": Fraction(4, 3),
    "tritone": Fraction(45, 32),
    "perfect_fifth": Fraction(3, 2),
    "minor_sixth": Fraction(8, 5),
    "major_sixth": Fraction(5, 3),
    "minor_seventh": Fraction(9, 5),
    "major_seventh": Fraction(15, 8),
    "octave": Fraction(2, 1),
}


@dataclass(frozen=True)
class Interval:
    """A named musical interval with its ratio and its width in cents."""

    name: str
    ratio: Fraction

    @property
    def cents(self) -> float:
        """Width of the interval in cents (1200 cents = one octave)."""
        import math

        return 1200 * math.log2(float(self.ratio))


def just_interval(name: str) -> Interval:
    """Return the just-intonation form of a named interval."""
    ratio = JUST_RATIOS[name]
    return Interval(name=name, ratio=ratio)


def equal_tempered_cents(semitones: int) -> float:
    """Width in cents of an interval of ``semitones`` half-steps, equal-tempered."""
    return 100.0 * semitones


def pythagorean_comma() -> float:
    """The Pythagorean comma, in cents.

    Twelve pure fifths (ratio 3/2) stacked slightly exceed seven octaves. The
    excess is the Pythagorean comma — roughly 23.46 cents — and is the
    reason no naive cyclic tuning scheme closes on itself. Zuckerkandl
    discusses the consequences; Boethius names the phenomenon differently.
    """
    import math

    twelve_fifths = 12 * 1200 * math.log2(3 / 2)
    seven_octaves = 7 * 1200.0
    return twelve_fifths - seven_octaves


def just_vs_equal(name: str, semitones: int) -> float:
    """Return the cent deviation of an equal-tempered interval from the just one.

    Positive means the equal-tempered interval is *wider* than the just one.
    For the major third (4 semitones), equal temperament is about 13.69
    cents sharp of just; this is audible.
    """
    return equal_tempered_cents(semitones) - just_interval(name).cents
