"""Shared helpers for the math / astronomy / music modules.

Use these only in notebooks where geometry, astronomy, or tone-ratio
computation genuinely helps understanding. The paper demonstration in a
module's ``problems.md`` is always authoritative; code is pedagogical support.

Submodules
----------
- :mod:`great.common.euclid`  — compass-and-straightedge primitives
- :mod:`great.common.ptolemy` — deferent + epicycle constructions
- :mod:`great.common.kepler`  — elliptical orbits + equal-area sweeps
- :mod:`great.common.music`   — interval ratios, Pythagorean vs equal-tempered
"""

from great.common import euclid, kepler, music, ptolemy

__all__ = ["euclid", "kepler", "music", "ptolemy"]
