# great.common

Lightweight Python helpers for the Mathematics, Natural Science, and Music modules. Do not import these from Theology / Philosophy / Language / Seminar notes.

## Modules

- [`euclid.py`](euclid.py) — compass-and-straightedge primitives: `segment`, `circle`, `intersect_circles`, `equilateral_triangle_apex`. Matches *Elements* Book I, Props. 1–3 style.
- [`ptolemy.py`](ptolemy.py) — `EpicycleOrbit` with `position`, `path`, and a `retrograde_segments` helper for reproducing planetary retrograde from *Almagest*.
- [`kepler.py`](kepler.py) — `Ellipse` with focal-polar radius, Kepler's equation solver, and a `swept_area` sanity check for the second law.
- [`music.py`](music.py) — `JUST_RATIOS`, `Interval` with `cents`, equal-tempered comparison, and the Pythagorean comma.

## Discipline

Notebooks that use these helpers belong in a module's `notebooks/` folder. The paper demonstration in `problems.md` / `solutions.md` is authoritative; code is a visualization and sanity check, not a replacement for drawing the diagram.

Convention for a notebook:

```python
import numpy as np
import matplotlib.pyplot as plt

from great.common import euclid, kepler, music, ptolemy
```

No wildcard imports. No package installs inside a notebook (add to `pyproject.toml` and rerun `uv sync`).
