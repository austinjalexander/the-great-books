"""Deferent + epicycle constructions for reproducing Ptolemy's *Almagest*.

Used in the Sophomore Mathematics astronomy cluster. The geocentric
epicycle-on-deferent model fits naked-eye observations of the planets to
roughly arc-minute accuracy — which is the main pedagogical point. Read
*Almagest* III–V before asking this module to reproduce anything.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class EpicycleOrbit:
    """A simple deferent + epicycle orbit, geocentric.

    Parameters
    ----------
    R
        Radius of the deferent (Earth-centered circle).
    r
        Radius of the epicycle.
    omega_deferent
        Angular velocity of the deferent center (radians per unit time).
    omega_epicycle
        Angular velocity of the planet around the epicycle center
        (radians per unit time).
    phase_deferent
        Starting angle of the deferent, in radians.
    phase_epicycle
        Starting angle of the epicycle, in radians.
    """

    R: float
    r: float
    omega_deferent: float
    omega_epicycle: float
    phase_deferent: float = 0.0
    phase_epicycle: float = 0.0

    def position(self, t: float) -> tuple[float, float]:
        """Return the ``(x, y)`` position of the planet at time ``t``."""
        theta_d = self.phase_deferent + self.omega_deferent * t
        theta_e = self.phase_epicycle + self.omega_epicycle * t
        cx = self.R * math.cos(theta_d)
        cy = self.R * math.sin(theta_d)
        x = cx + self.r * math.cos(theta_e)
        y = cy + self.r * math.sin(theta_e)
        return (x, y)

    def path(self, t_start: float, t_end: float, steps: int = 1000) -> list[tuple[float, float]]:
        """Return the path of the planet from ``t_start`` to ``t_end``."""
        if steps < 2:
            raise ValueError("steps must be >= 2")
        dt = (t_end - t_start) / (steps - 1)
        return [self.position(t_start + i * dt) for i in range(steps)]


def retrograde_segments(
    orbit: EpicycleOrbit, t_start: float, t_end: float, steps: int = 1000
) -> list[tuple[float, float]]:
    """Return time-stamps of retrograde motion within ``[t_start, t_end]``.

    Retrograde occurs when the geocentric ecliptic longitude momentarily
    *decreases*. This is the phenomenon Ptolemy's epicycle is designed to
    capture, and exploring it in a notebook makes the geometric account far
    more vivid than it is on paper.
    """
    if steps < 3:
        raise ValueError("steps must be >= 3")
    dt = (t_end - t_start) / (steps - 1)
    longitudes = []
    for i in range(steps):
        x, y = orbit.position(t_start + i * dt)
        longitudes.append(math.atan2(y, x))
    segments: list[tuple[float, float]] = []
    in_retrograde = False
    seg_start = 0.0
    for i in range(1, steps):
        d_lambda = longitudes[i] - longitudes[i - 1]
        if d_lambda > math.pi:
            d_lambda -= 2 * math.pi
        if d_lambda < -math.pi:
            d_lambda += 2 * math.pi
        going_backward = d_lambda < 0
        t_i = t_start + i * dt
        if going_backward and not in_retrograde:
            seg_start = t_i
            in_retrograde = True
        elif not going_backward and in_retrograde:
            segments.append((seg_start, t_i))
            in_retrograde = False
    if in_retrograde:
        segments.append((seg_start, t_start + (steps - 1) * dt))
    return segments
