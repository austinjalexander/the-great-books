# Math and code style

Most of this repo is prose and citations. A small fraction — the Mathematics, Natural Science, and Music modules — benefits from mathematical notation and, occasionally, Python. This rule applies to those.

## Mathematical notation in markdown

- Inline math with `$...$`; display math with `$$...$$`. Avoid `\(...\)` in markdown.
- Prefer the author's own notation where faithful: $AB$ for the line segment in Euclid; $\vec{F} = m\vec{a}$ for Newton; $\nabla \times \vec{E} = -\partial_t \vec{B}$ for Maxwell.
- Greek letters spelled out in LaTeX: `\alpha`, `\beta`, `\gamma`, `\Delta`. Use `\varepsilon` rather than `\epsilon` when the script form matters.
- Vectors: `\vec{v}` (inline), or bold-face `\mathbf{v}` where typographically preferable. Pick one per module and stay consistent.
- Differentials: `\mathrm{d}x` (upright). Partial derivatives: `\partial_t`, `\partial / \partial x`.
- Equations in derivations are numbered only when later cross-referenced. No orphan numbers.
- A single `$...$` per claim. Long symbolic chains belong in display math.

## Physics and geometry conventions

- Angles in radians unless the primary text (Ptolemy, Apollonius, Newton) uses degrees or chord-tables.
- Coordinates named after the author where it matters: Cartesian $(x, y)$ for Descartes; plane-polar $(r, \theta)$ for Kepler; $(R, \theta, \varphi)$ for the celestial sphere.
- Magnitudes and units: always carry units through a calculation; introduce `pint` in a notebook if a calculation mixes systems.
- Limiting cases are cited: "as $e \to 0$ at fixed semi-major axis, a Kepler ellipse becomes a circle," with a passage citation to the relevant proposition.

## Python

- Python 3.12. Dependencies managed by `uv` (see `pyproject.toml`).
- Notebooks live in a module's `notebooks/` folder, named `NN-descriptive-slug.ipynb`.
- Notebooks are for *exploration and visualization*, not substitutes for paper demonstration. The paper demonstration in `problems.md` is authoritative.
- A notebook opens with a markdown cell naming: the primary text and proposition being explored; what the notebook adds that paper cannot easily show (usually: a fit, a plot, or a numerical check).
- Imports block at the top. One cell. Follow:
  ```python
  import numpy as np
  import matplotlib.pyplot as plt

  from great.common import euclid, ptolemy, kepler, music
  ```
- No `import *`. No package installs inside a notebook — add them to `pyproject.toml` and rerun `uv sync`.
- Functions before calls. No hidden state across cells beyond the imports cell and a single "constants" cell.

## `great/common` conventions

Helpers live under `great/common/` and are named by their subject:

- `great.common.euclid` — construction primitives on a `matplotlib` axes: `segment`, `circle`, `intersect_circles`, `equilateral_triangle_apex`.
- `great.common.ptolemy` — deferent + epicycle: `EpicycleOrbit` with `position`, `path`, and `retrograde_segments`.
- `great.common.kepler` — `Ellipse` and `swept_area` for visualizing the second law.
- `great.common.music` — `JUST_RATIOS`, `Interval`, and the existing tuning helpers (inspect signatures before use).

Helper functions are *pedagogical*. They favor clarity and single-purpose over efficiency. No vectorized cleverness at the cost of readability.

## Plots

- One idea per plot. If it has two y-axes and three legends, it is two plots pretending to be one.
- Axes always labeled with the quantity and its unit.
- A title names the claim the plot is evidence for, not "Figure 3."
- Saved plots live next to the notebook as `NN-slug.png` if referenced from `notes.md`; otherwise stay inside the notebook.

## Anti-patterns

- Paraphrasing a paper demonstration in `notes.md` instead of giving the demonstration.
- Using Python to hide a step you have not understood on paper.
- Long floating blocks of code without markdown cells explaining the demonstration they belong to.
- Inconsistent notation between `notes.md`, `problems.md`, and the module's notebooks.
