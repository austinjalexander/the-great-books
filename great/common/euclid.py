"""Compass-and-straightedge primitives for reproducing Euclid's constructions.

These are *pedagogical*. They favor clarity and faithfulness to the
``Elements`` over efficiency. Always draw the construction on paper first;
the notebook rendering is a check, not a substitute.

Typical usage::

    import matplotlib.pyplot as plt
    from great.common import euclid

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")

    A = (0.0, 0.0)
    B = (1.0, 0.0)

    euclid.segment(A, B, ax=ax, label="AB")
    C = euclid.equilateral_triangle_apex(A, B)
    euclid.segment(A, C, ax=ax)
    euclid.segment(B, C, ax=ax)
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from matplotlib.axes import Axes

Point = tuple[float, float]


def segment(a: Point, b: Point, *, ax: Axes, label: str | None = None) -> None:
    """Draw the line segment from ``a`` to ``b``."""
    ax.plot([a[0], b[0]], [a[1], b[1]], color="black", linewidth=1)
    if label is not None:
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        ax.annotate(label, (mx, my), textcoords="offset points", xytext=(6, 6))


def circle(center: Point, radius: float, *, ax: Axes) -> None:
    """Draw a circle with the given ``center`` and ``radius``."""
    angles = [i * 2 * math.pi / 360 for i in range(361)]
    xs = [center[0] + radius * math.cos(t) for t in angles]
    ys = [center[1] + radius * math.sin(t) for t in angles]
    ax.plot(xs, ys, color="black", linewidth=0.8)


def distance(a: Point, b: Point) -> float:
    """Euclidean distance between two points."""
    return math.hypot(a[0] - b[0], a[1] - b[1])


def equilateral_triangle_apex(a: Point, b: Point, *, above: bool = True) -> Point:
    """Return the apex ``C`` of the equilateral triangle on base ``AB``.

    This is Proposition I.1 of the *Elements*: given a finite straight line
    ``AB``, construct an equilateral triangle on it. The apex lies on the
    perpendicular bisector of ``AB``, at distance ``|AB| * sqrt(3) / 2``.
    """
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    perp = (-dy, dx) if above else (dy, -dx)
    length = math.hypot(*perp)
    ux, uy = perp[0] / length, perp[1] / length
    half_base = distance(a, b) / 2
    h = half_base * math.sqrt(3)
    return (mx + ux * h, my + uy * h)


def intersect_circles(c1: Point, r1: float, c2: Point, r2: float) -> tuple[Point, Point] | None:
    """Return the two intersection points of two circles, or ``None``.

    Used throughout Book I — Propositions 1, 2, 3 all rest on drawing two
    circles and picking one of their intersection points.
    """
    d = distance(c1, c2)
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return None
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h2 = r1**2 - a**2
    if h2 < 0:
        return None
    h = math.sqrt(h2)
    ex = (c2[0] - c1[0]) / d
    ey = (c2[1] - c1[1]) / d
    px, py = c1[0] + a * ex, c1[1] + a * ey
    return ((px + h * ey, py - h * ex), (px - h * ey, py + h * ex))
