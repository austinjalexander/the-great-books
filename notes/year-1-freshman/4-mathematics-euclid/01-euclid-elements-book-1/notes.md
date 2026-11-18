# Reading Notes — Euclid, *Elements*, Book I

**Evidence status:** existing teaching/reference notes; learner authorship and study are not established. Record actual attempts in `learner-work.md`. These notes do not complete the module.

> Structure, passage-cited summaries, key terms, puzzles, and connections. Cite by book and item number: Def. I.1, Post. I.5, C.N. I.1, Prop. I.47.

## Edition used

Heath, *The Thirteen Books of Euclid's Elements*, 2nd ed., vol. I (Dover, 1956). Proposition numbers are Euclid's own and are stable across all editions; Heath's page numbers are not cited here.

## Structure of Book I

Book I has four distinct acts:

- **Act I — Foundations** (beginning of Book I): 23 definitions, 5 postulates, 5 common notions.
- **Act II — Congruence and the triangle** (Props. 1–26): constructions of equilateral triangles, segments, angles; the three classical congruence theorems (SAS at I.4, SSS at I.8, ASA/AAS at I.26); base-angles of isosceles triangles (I.5, the *pons asinorum*).
- **Act III — Parallels and angle-sum** (Props. 27–32): the theory of parallel lines, culminating in Prop. I.32 that the exterior angle of a triangle equals the sum of the two remote interior angles, and the three interior angles sum to two right angles.
- **Act IV — Area and the Pythagorean theorem** (Props. 33–48): parallelograms on the same base and between the same parallels are equal in area; the Pythagorean theorem at I.47; its converse at I.48.

The book is engineered so that I.1 is the minimal nontrivial construction and I.47 is the maximal nontrivial theorem; every intermediate proposition earns its keep.

## The foundations

### 23 definitions (Def. I.1 – I.23)

A short, passage-cited summary of each:

- **Def. I.1** — *A point is that which has no part.*
  Negative definition; intuitively, a location with no extension.
- **Def. I.2** — *A line is breadthless length.*
  Again negative; "line" in Euclid is what we call a **curve**, not only straight lines.
- **Def. I.3** — *The extremities of a line are points.*
- **Def. I.4** — *A straight line is a line which lies evenly with the points on itself.*
  Heath's clearest gloss: a straight line is a line that is "rigid" under sliding end-to-end.
- **Def. I.5–I.7** — surface, its extremities (lines), and plane surface (defined analogously to the straight line).
- **Def. I.8** — *A plane angle is the inclination to one another of two lines in a plane which meet one another and do not lie in a straight line.*
- **Def. I.9** — rectilineal angle (when the two lines are straight).
- **Def. I.10** — right angle, and therewith **perpendicular** and the definition of right-angled figures.
- **Def. I.11–I.12** — obtuse and acute angles.
- **Def. I.13–I.14** — boundary and figure.
- **Def. I.15** — circle.
  "A plane figure contained by one line [curve] such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another." The center follows at I.16.
- **Def. I.16** — center of a circle.
- **Def. I.17** — diameter.
- **Def. I.18** — semicircle.
- **Def. I.19** — rectilineal figures: trilateral, quadrilateral, multilateral.
- **Def. I.20** — three kinds of triangle by sides: equilateral, isosceles, scalene.
- **Def. I.21** — three kinds by angles: right-angled, obtuse-angled, acute-angled.
- **Def. I.22** — four kinds of quadrilateral: square, oblong (rectangle), rhombus, rhomboid; the rest are "trapezia."
- **Def. I.23** — parallel straight lines: "straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction." **This is where the trouble of the fifth postulate will land.**

### 5 postulates (Post. I.1 – I.5)

*Let the following be postulated:*

1. **Post. I.1** — To draw a straight line from any point to any point.
2. **Post. I.2** — To produce a finite straight line continuously in a straight line.
3. **Post. I.3** — To describe a circle with any center and radius.
4. **Post. I.4** — That all right angles are equal to one another.
5. **Post. I.5** — *That, if a straight line falling on two straight lines makes the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet on that side on which the angles are less than two right angles.*

The first four are brief and convictional; the fifth is three times as long and *feels* like a theorem that should be demonstrable from simpler principles. For two millennia geometers tried to prove Post. I.5 from the other four; Lobachevski will show Senior year that it cannot be done.

### 5 common notions (C.N. I.1 – I.5)

*Common Notions* (or "axioms") — truths not specific to geometry:

1. **C.N. I.1** — Things equal to the same thing are equal to one another.
2. **C.N. I.2** — If equals are added to equals, the wholes are equal.
3. **C.N. I.3** — If equals are subtracted from equals, the remainders are equal.
4. **C.N. I.4** — Things which coincide with one another are equal to one another.
5. **C.N. I.5** — The whole is greater than the part.

## Dependency graph of propositions

A coarse map (built by asking, for each Prop., which earlier Props. it cites):

- **I.1** → requires only Post. 1, Post. 3, C.N. 1, Def. 15.
- **I.2, I.3** → use I.1; let us transport a length.
- **I.4** (SAS) → proved by superposition, using C.N. 4 directly.
- **I.5** (*pons asinorum*) → uses I.4, I.3.
- **I.6** → converse of I.5, proved by *reductio*.
- **I.8** (SSS) → uses I.7.
- **I.13–I.15** → theorems about supplementary / vertical angles.
- **I.16** (exterior-angle theorem) → uses I.15, I.4. **Does not use Post. 5.** Crucial for neutral geometry.
- **I.17** → angles of a triangle are less than two right angles. Again no Post. 5.
- **I.27–I.28** → two constructions of parallel lines *without* Post. 5.
- **I.29** — **the first proposition that uses Post. 5** — converse of I.27.
- **I.32** → exterior angle = sum of the two remote interior angles; angle sum = two right angles. Both rest on I.29, hence on Post. 5.
- **I.33–I.46** → parallelograms and areas.
- **I.47** (Pythagorean theorem) → uses I.4, I.14, I.31, I.41, I.46; hence indirectly uses Post. 5 through I.29/I.32.
- **I.48** → converse of I.47, uses I.47, I.8, I.3.

So: **Propositions I.1 – I.28 form "neutral geometry,"** holding in Euclidean, spherical, and hyperbolic geometries alike. Propositions I.29 – I.48 require Post. 5. This classification is the modern way to see what Lobachevski's *Geometrical Researches* (Senior Mathematics) is really doing.

## Passage-cited summary (selected)

- **I.1** — On any given finite straight line, construct an equilateral triangle. *Proof.* Draw circle on A with radius AB; draw circle on B with radius BA; they intersect at C; AC = AB = BC by Def. I.15, hence by C.N. I.1 the triangle is equilateral. *Quod erat demonstrandum.*
- **I.4** — If two triangles have two sides and the included angle of one equal to the corresponding two sides and included angle of the other, then the two triangles are equal in all respects. *Proof by superposition.* The weakest link in Euclid's exposition — Heath (vol. I, commentary on I.4) discusses at length why moderns treat this as an axiom.
- **I.5** — In an isosceles triangle, the base angles are equal; also, the angles under the base (when the equal sides are produced) are equal. *Proof* uses I.3 to cut off equal segments and I.4 twice. Dubbed *pons asinorum* ("bridge of asses") in the Middle Ages.
- **I.16** — The exterior angle of a triangle is greater than either of the two remote interior angles. **No use of Post. 5.** The argument constructs a point midway along the opposite side and reasons by I.4. Fails on a sphere (where large triangles can have exterior angles smaller than either remote interior angle).
- **I.29** — If a straight line falls on two parallel straight lines, it makes the alternate angles equal, the exterior angle equal to the interior and opposite angle, and the sum of the interior angles on the same side equal to two right angles. **This is the first proposition that uses Post. 5.**
- **I.32** — In any triangle, if one side is produced, the exterior angle equals the sum of the two remote interior angles, and the three interior angles sum to two right angles.
- **I.47** — In a right-angled triangle, the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.
- **I.48** — Converse: if the square on one side equals the sum of the squares on the other two, then the angle contained by those two sides is right.

## Key terms

| Term | Original | Working definition | Where |
|------|----------|--------------------|-------|
| point | σημεῖον (*sēmeion*) | that which has no part | Def. I.1 |
| straight line | εὐθεῖα γραμμή (*eutheia grammē*) | line "lying evenly with the points on itself" | Def. I.4 |
| right angle | ὀρθή γωνία (*orthē gōnia*) | angle equal to its supplement | Def. I.10 |
| circle | κύκλος (*kyklos*) | figure whose radii are equal | Def. I.15 |
| parallel | παράλληλος (*parallēlos*) | coplanar straight lines never meeting | Def. I.23 |
| postulate | αἴτημα (*aitēma*) | a specifically geometric request | introduction to the postulates |
| common notion | κοινὴ ἔννοια (*koinē ennoia*) | a general truth, not limited to geometry | introduction to the common notions |
| demonstration | ἀπόδειξις (*apodeixis*) | the chain from premises to the theorem | throughout; also used by Aristotle in *Posterior Analytics* I.2 |

## Puzzles and questions raised while reading

Leave these unanswered here; work them in [`discussion.md`](discussion.md).

- Why does Euclid separate postulates from common notions? They both seem to be "things assumed without proof."
- Def. I.4 ("a straight line lies evenly with the points on itself") — what does "lies evenly" mean? Is it meant as a definition at all, or as a recognition?
- Post. I.5 is obviously different in character from Posts. I.1–I.4. Why did Euclid state it as a postulate rather than a theorem? Is it because he tried and failed to prove it?
- I.4 is proved by "superposition" — moving one triangle onto another. Is this a legitimate proof technique in Euclid's own terms? (Heath and many modern geometers say no.)
- Why are I.16 and I.17 *theorems* in neutral geometry but nonetheless *true* in spherical geometry only locally? What does "local" versus "global" even mean here (it has no role in Euclid)?
- In I.29, the appeal to Post. 5 looks almost ceremonial — the main work is done by I.16. Is Post. 5 really needed here, or could a subtler proof avoid it?
- Could a medieval commentator have replaced Post. 5 with Playfair's axiom ("through a point outside a line, there is exactly one parallel") without deductive loss?

## Connections

**Backward** — nothing within this repo. Euclid is the first module.

**Forward** — explicit links:

- 1-Philosophy `11-aristotle-posterior-analytics/` — Aristotle's *Posterior Analytics* I.2 on the structure of demonstrative science. Aristotle says science proceeds from prior, better-known, more necessary premises; Euclid is the concrete instance.
- 1-Philosophy `13-aquinas-proemium-posterior-analytics/` — Aquinas's short *Proemium* explicitly places geometry as the model liberal art.
- 2-Mathematics `02-ptolemy-almagest/`, `04-apollonius-conics/`, `05-kepler-epitome-astronomia-nova/` — all three presuppose Book I throughout.
- 3-Mathematics `02-descartes-geometry/` — Descartes's *Geometry* explicitly puts itself *against* Book I's synthetic method. The confrontation is the whole point of the module.
- 3-Natural-Science `03-newton-principia-junior/` — Newton writes in Euclidean style; *Principia* Book I reads as Euclid continued under mechanics.
- 4-Mathematics `02-lobachevski-parallels/` — Lobachevski begins: "every reader has found . . . the theory of parallels in Euclid difficult." His treatise investigates whether Post. I.5 can be replaced.

## First-read summary (3–5 sentences, in your own words)

*(Write this in **your** own voice, before consulting any commentary. Leaving the space here, intentionally.)*
