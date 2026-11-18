"""Elliptical orbits and the equal-area law, for Kepler's *Astronomia Nova*.

The point of putting Kepler in a notebook is not to *solve* Kepler's
equation for the student — that is a calculus exercise from the primary
text — but to make Kepler's first and second laws visible: the focus of the
ellipse really is the Sun's place, and equal areas really are swept in
equal times.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Ellipse:
    """A Kepler ellipse with the focus at the origin.

    Parameters
    ----------
    a
        Semi-major axis.
    e
        Eccentricity, ``0 <= e < 1``.
    argument_of_periapsis
        Angle from the positive x-axis to the periapsis, in radians.
    """

    a: float
    e: float
    argument_of_periapsis: float = 0.0

    def radius_at_true_anomaly(self, nu: float) -> float:
        """Orbital radius as a function of true anomaly ``nu`` (radians)."""
        p = self.a * (1 - self.e**2)
        return p / (1 + self.e * math.cos(nu))

    def position_at_true_anomaly(self, nu: float) -> tuple[float, float]:
        """Position ``(x, y)`` with the focus at the origin."""
        r = self.radius_at_true_anomaly(nu)
        theta = nu + self.argument_of_periapsis
        return (r * math.cos(theta), r * math.sin(theta))

    def path(self, steps: int = 720) -> list[tuple[float, float]]:
        """Full closed orbit as a list of ``(x, y)`` points."""
        if steps < 2:
            raise ValueError("steps must be >= 2")
        return [self.position_at_true_anomaly(2 * math.pi * i / steps) for i in range(steps + 1)]


def solve_kepler(M: float, e: float, tol: float = 1e-10, max_iter: int = 64) -> float:
    """Solve Kepler's equation ``M = E - e sin E`` for ``E`` (Newton's method)."""
    E = M if e < 0.8 else math.pi
    for _ in range(max_iter):
        f = E - e * math.sin(E) - M
        fp = 1 - e * math.cos(E)
        dE = -f / fp
        E += dE
        if abs(dE) < tol:
            return E
    return E


def true_anomaly_at_time(ellipse: Ellipse, t: float, period: float) -> float:
    """Return the true anomaly at elapsed time ``t`` in a circular-period ``period``."""
    M = 2 * math.pi * (t / period)
    E = solve_kepler(M, ellipse.e)
    nu = 2 * math.atan2(
        math.sqrt(1 + ellipse.e) * math.sin(E / 2),
        math.sqrt(1 - ellipse.e) * math.cos(E / 2),
    )
    return nu


def swept_area(
    ellipse: Ellipse, t0: float, t1: float, period: float, steps: int = 500
) -> float:
    """Area swept by the focal radius between times ``t0`` and ``t1``.

    Uses the shoelace formula on a polygonal approximation between the two
    positions and the focus. Kepler's second law: for any ``t1 - t0`` of
    fixed length, this returns the same value regardless of where in the
    orbit ``t0`` is.
    """
    if steps < 2:
        raise ValueError("steps must be >= 2")
    dt = (t1 - t0) / (steps - 1)
    area = 0.0
    prev = ellipse.position_at_true_anomaly(true_anomaly_at_time(ellipse, t0, period))
    for i in range(1, steps):
        t = t0 + i * dt
        curr = ellipse.position_at_true_anomaly(true_anomaly_at_time(ellipse, t, period))
        area += 0.5 * abs(prev[0] * curr[1] - prev[1] * curr[0])
        prev = curr
    return area
