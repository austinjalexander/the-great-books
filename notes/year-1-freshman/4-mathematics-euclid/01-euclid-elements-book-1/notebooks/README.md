# Notebooks — Euclid, *Elements*, Book I

Optional Python support. The paper demonstration in [`../problems.md`](../problems.md) and [`../solutions.md`](../solutions.md) is authoritative; code here is visualization and sanity check.

Helpers used: [`../../../../../great/common/euclid.py`](../../../../../great/common/euclid.py).

## Suggested notebooks

- `01-construct-equilateral-triangle.ipynb` — reproduce Prop. I.1 with `great.common.euclid.intersect_circles` and draw the construction. Verify AC = AB = BC numerically.
- `02-pons-asinorum.ipynb` — animate Prop. I.5 by varying the base length and checking that the two base angles remain equal.
- `03-exterior-angle-on-sphere.ipynb` — show, on a `matplotlib` great-circle plot, a spherical triangle for which Prop. I.16 fails; identify the broken assumption in Euclid's proof.
- `04-pythagorean-theorem.ipynb` — visualize Prop. I.47 with the three squares and the auxiliary line $AL$; confirm areas numerically.

## Style

See [`.cursor/rules/math-and-code-style.mdc`](../../../../../.cursor/rules/math-and-code-style.mdc) for plot and import conventions.
