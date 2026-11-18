# Solutions — Euclid, *Elements*, Book I

> Worked demonstrations with explicit **"Check."** steps. Do not read until you have attempted each problem in [`problems.md`](problems.md). Every citation is to Book I unless otherwise noted.

## 1. State and classify

*(Write out the 23 definitions, 5 postulates, 5 common notions from memory; this is a recall exercise, not a demonstration. The classification table belongs in your own hand.)*

## 2. Postulate 5, in full

**Euclid's form**:

> If a straight line falling on two straight lines makes the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet on that side on which the angles are less than two right angles.

**Contrapositive** (exercise form):

> If two straight lines, produced indefinitely on both sides, do not meet, then a straight line falling on them makes the interior angles on each side equal to two right angles.

In other words: parallel lines are exactly the pairs on which any transversal produces interior angles summing to $2$ right angles.

**Check.** The contrapositive is Playfair's axiom's *uniqueness* half: given parallel lines, the transversal angles are determined. The converse (interior angles sum to two right angles ⇒ lines parallel) is Prop. I.28 and does *not* require Post. 5.

---

## 3. Prop. I.1 — equilateral triangle on *AB*

**Construction.**

1. By **Post. I.3**, with center $A$ and radius $AB$, describe circle $\mathrm{BCD}$.
2. By **Post. I.3**, with center $B$ and radius $BA$, describe circle $\mathrm{ACE}$.
3. The two circles meet at a point $C$ (on each side of $AB$; take either intersection).
4. By **Post. I.1**, join $AC$ and $BC$.

**Demonstration.**

- Since $A$ is the center of circle $\mathrm{BCD}$, **Def. I.15** gives $AC = AB$.
- Since $B$ is the center of circle $\mathrm{ACE}$, **Def. I.15** gives $BC = BA$.
- Therefore $AC = AB$ and $BC = AB$, whence by **C.N. I.1** $AC = BC$.
- Hence $AB = AC = BC$, and triangle $ABC$ is equilateral. *Q.E.F.*

**Check.** Two circles of radius $|AB|$ centered at $A$ and $B$ intersect iff $|AB| \le 2|AB|$ (which is trivially true); they are distinct iff $A \neq B$. The construction therefore succeeds for any non-degenerate segment. Limiting case: as $|AB| \to 0$, the triangle collapses to a point, consistent with the construction.

---

## 4. Prop. I.2 — transport a length

**Setup.** Given a point $A$ and a segment $BC$, place at $A$ a segment equal in length to $BC$.

**Construction.**

1. By **Post. I.1**, join $AB$.
2. By **I.1**, construct equilateral triangle $ABD$ on $AB$.
3. By **Post. I.2**, produce $DA$ to a point $E$ such that $E$ lies on the line $DA$ beyond $A$; produce $DB$ to a point $F$ beyond $B$.
4. By **Post. I.3**, with center $B$ and radius $BC$, describe circle $\mathrm{CGH}$, meeting $DF$ at $G$.
5. By **Post. I.3**, with center $D$ and radius $DG$, describe circle $\mathrm{GKL}$, meeting $DE$ at $L$.

**Demonstration.**

- $BG = BC$ (both radii of $\mathrm{CGH}$, by **Def. I.15**).
- $DG = DL$ (both radii of $\mathrm{GKL}$, by **Def. I.15**).
- $DB = DA$ (sides of equilateral $ABD$, **I.1**).
- Hence $AL = DL - DA = DG - DB = BG = BC$.

Thus $AL = BC$. *Q.E.F.*

**Check.** The construction works from a *fixed* compass: the compass may be opened and then collapsed; it need not "carry" lengths directly. The whole point of I.2 is to earn the right to transport a length from one place to another using only Post. I.1–3 plus I.1.

---

## 5. Prop. I.4 — SAS congruence

**Setup.** Triangles $ABC$ and $DEF$ with $AB = DE$, $AC = DF$, and $\angle BAC = \angle EDF$.

**Demonstration** (by superposition).

- Apply triangle $ABC$ to triangle $DEF$ so that $A$ is placed on $D$ and $AB$ along $DE$.
- Since $AB = DE$, $B$ falls on $E$.
- Since $\angle BAC = \angle EDF$, $AC$ falls along $DF$.
- Since $AC = DF$, $C$ falls on $F$.
- Since $B$ coincides with $E$ and $C$ coincides with $F$, $BC$ coincides with $EF$.
- By **C.N. I.4** ("things which coincide with one another are equal to one another"), $BC = EF$, and the two triangles are equal in all respects. *Q.E.D.*

**Check / critique.** Superposition is the weakest step in Euclid's formal program. C.N. I.4 says coinciding figures are *equal*; it does not explicitly grant the *motion* that realizes the coincidence. Hilbert (1899) takes I.4 as an axiom (the SAS axiom) and Euclid's "proof" becomes unnecessary. For the self-study reader, the productive response is neither to reject Euclid nor to pretend the proof is airtight; it is to notice exactly what gets smuggled in, and carry that noticing forward to *Posterior Analytics* I.2, where the question "what counts as an axiom?" becomes explicit.

---

## 6. Prop. I.5 — *pons asinorum*

**Setup.** Isosceles triangle $ABC$ with $AB = AC$. Produce $AB$ to $D$ and $AC$ to $E$ (both by **Post. I.2**).

**Construction.**

1. On $BD$, mark off $BF$ (by **I.3**) equal to some length less than $BD$; on $CE$, mark off $CG = BF$ (by **I.3**).
2. Join $FC$ and $GB$ (**Post. I.1**).

**Demonstration.**

- In triangles $AFC$ and $AGB$:
  - $AF = AG$ (sum of equal segments on equal sides: $AF = AB + BF = AC + CG = AG$, by **C.N. I.2**).
  - $AC = AB$ (given, swapping sides).
  - $\angle FAC = \angle GAB$ (same angle).
- By **I.4**, $\triangle AFC = \triangle AGB$ in all respects, so $FC = GB$ and $\angle AFC = \angle AGB$ and $\angle ACF = \angle ABG$.
- In triangles $BFC$ and $CGB$:
  - $BF = CG$ (by construction).
  - $FC = GB$ (just proved).
  - $\angle BFC = \angle CGB$ (just proved).
- By **I.4** again, $\triangle BFC = \triangle CGB$, so $\angle FBC = \angle GCB$ (these are the angles under the base) and $\angle BCF = \angle CBG$.
- Finally, $\angle ABC = \angle ABG - \angle CBG = \angle ACF - \angle BCF = \angle ACB$ (by **C.N. I.3**).
- Hence $\angle ABC = \angle ACB$, and the angles under the base ($\angle FBC$ and $\angle GCB$) are also equal. *Q.E.D.*

**Check.** Pappus's alternative proof sidesteps the extensions $BD$, $CE$: compare $\triangle ABC$ with itself, mapping $A \to A$, $B \to C$, $C \to B$. Then by **I.4** (using $AB = AC$, $AC = AB$, $\angle BAC = \angle CAB$) the triangle is congruent to its mirror image, whence $\angle B = \angle C$ directly. Pappus's proof is shorter but borrows a subtler "reflection" operation; Euclid's proof is more elementary and fits I.4's plain form.

---

## 7. Prop. I.8 — SSS congruence

*(Outline, not a full proof — fill in the construction on paper.)*

Given triangles $ABC$ and $DEF$ with $AB = DE$, $BC = EF$, $AC = DF$.

Superpose $\triangle ABC$ onto $\triangle DEF$ by placing $B$ on $E$ and $BC$ along $EF$. Since $BC = EF$, $C$ coincides with $F$. Then $A$ must lie at a point equidistant from $E$ and $F$ with distances $AB$ and $AC$ respectively; but by **I.7** (the uniqueness lemma: no two distinct points on the same side of a line can both be at the given distances from its endpoints), there is exactly one such point, which must be $D$. Hence $A$ coincides with $D$, and by **C.N. I.4** the triangles are equal in all respects. *Q.E.D.*

**Check.** I.7 is the workhorse here. Without it, "A must lie at $D$" is not justified. This dependence is why Euclid proved I.7 first and only then I.8.

---

## 8. Prop. I.16 — exterior angle greater than remote interior

**Setup.** Triangle $ABC$; produce $BC$ through $C$ to $D$ (by **Post. I.2**); the exterior angle is $\angle ACD$.

**Construction.**

1. Bisect $AC$ at $E$ (by **I.10**); join $BE$ (**Post. I.1**); produce $BE$ to $F$ such that $EF = BE$ (by **I.3** and **Post. I.2**); join $CF$ (**Post. I.1**).

**Demonstration.**

- In triangles $AEB$ and $CEF$:
  - $AE = CE$ (construction).
  - $BE = EF$ (construction).
  - $\angle AEB = \angle CEF$ (vertical angles, by **I.15**).
- By **I.4**, $\triangle AEB = \triangle CEF$, so $\angle BAE = \angle ECF$.
- Now $\angle ACD > \angle ECF$ (since $F$ lies "inside" the exterior angle $\angle ACD$ by the construction — see **Check.** below for the force of this step).
- Hence $\angle ACD > \angle BAE = \angle BAC$, and the exterior angle is greater than the remote interior $\angle A$.
- Similarly, bisecting $BC$ and producing analogously, $\angle ACD > \angle ABC$. *Q.E.D.*

**Check.** The unstated assumption: "$F$ lies inside the exterior angle $\angle ACD$." On a sphere, for a sufficiently large triangle, this fails — the point $F$ can swing *around* past $CD$, and the exterior angle can be smaller than $\angle A$ or $\angle B$. Euclid's proof of I.16 therefore presupposes an *unboundedness* property of the plane that is not an explicit postulate. This is one of the gaps Lobachevski and Hilbert would later name.

Thus: I.16 is "neutral" with respect to Post. I.5 (it does not use the parallel postulate), but it is *not* neutral with respect to the underlying space being flat and infinite. That is the right lesson to carry to Senior Mathematics.

---

## 9. Prop. I.20 — triangle inequality

*(Outline; fill in on paper.)* In triangle $ABC$, produce $BA$ to $D$ so that $AD = AC$; join $DC$. Then $\triangle ACD$ is isosceles, so by **I.5** $\angle ACD = \angle ADC$. Hence $\angle BCD > \angle ADC = \angle BDC$, so by **I.19** (greater angle opposite greater side) $BD > BC$. But $BD = BA + AD = BA + AC$. Therefore $BA + AC > BC$. *Q.E.D.*

**Check.** The same inequality holds by symmetry for the other two pairs of sides. Degenerate limit: if $A$ lies *on* segment $BC$, then $BA + AC = BC$, matching the strict inequality becoming equality.

---

## 10. Prop. I.26 — ASA / AAS

*(Standard two-case superposition argument; consult Heath if stuck. Both cases reduce to I.4 after an initial cut-and-compare step.)*

---

## 11. Prop. I.27 — parallels without Post. 5

**Setup.** Straight line $EF$ falls on $AB$ and $CD$ making alternate angles $\angle AEF = \angle EFD$.

**Demonstration (by reductio).** Suppose $AB$ and $CD$ are not parallel; then they meet, say on the side of $B$ and $D$, at a point $G$. Then $\triangle EFG$ has $\angle AEF$ as an exterior angle and $\angle EFG (= \angle EFD)$ as a remote interior angle. By **I.16**, $\angle AEF > \angle EFD$. But $\angle AEF = \angle EFD$ by hypothesis — contradiction. Symmetrically, $AB$ and $CD$ cannot meet on the other side. Hence they are parallel, by **Def. I.23**. *Q.E.D.*

**Check.** The proof uses only I.16, I.15, Def. I.23, and *reductio* — specifically not Post. 5. This is why "equal alternate angles ⇒ parallel" is a neutral-geometry theorem.

---

## 12. Prop. I.29 — properties of parallels

**Setup.** Straight line $EF$ falls on the parallels $AB \parallel CD$ at points $G$ and $H$.

**Demonstration.** Suppose the alternate angles $\angle AGH$ and $\angle GHD$ are not equal. Then one is greater; suppose $\angle AGH > \angle GHD$. Add $\angle BGH$ to both: by **C.N. I.2**, $\angle AGH + \angle BGH > \angle GHD + \angle BGH$. The left side equals two right angles (by **I.13**). Hence $\angle GHD + \angle BGH < 2$ right angles. **By Post. I.5**, the lines $AB$ and $CD$ produced on the side of $B$ and $D$ must meet — contradicting that they are parallel. Hence $\angle AGH = \angle GHD$.

The exterior-angle and co-interior-angle statements follow from this by I.13 and simple arithmetic.

**Check.** This is the very *first* proposition of Book I that invokes Post. 5. Every earlier proposition is neutral. The appeal is stark: without Post. 5, the argument has no grip — we could not conclude that lines *must* meet given the inequality of interior angles.

---

## 13. Prop. I.32 — exterior angle; angle sum

**Setup.** Triangle $ABC$; produce $BC$ to $D$.

**Construction.** Through $C$ draw $CE$ parallel to $BA$ (by **I.31**).

**Demonstration.**

- $\angle ACE = \angle BAC$ (alternate angles on parallels $CE \parallel BA$ cut by $CA$, by **I.29**).
- $\angle ECD = \angle ABC$ (corresponding angles, by **I.29**).
- Hence $\angle ACD = \angle ACE + \angle ECD = \angle BAC + \angle ABC$ — the exterior angle equals the sum of the two remote interior angles.
- Adding $\angle ACB$ to both sides: $\angle ACD + \angle ACB = \angle BAC + \angle ABC + \angle ACB$. The left side is two right angles (**I.13**). Hence the three interior angles sum to two right angles. *Q.E.D.*

**Check.** Every step uses I.29, which uses Post. I.5. So "the angles of a triangle sum to $180°$" is equivalent, in the presence of Books I.1–I.28, to Post. I.5. On a sphere the sum exceeds $180°$; in hyperbolic geometry it falls short. This proposition is the cleanest marker that we are in the Euclidean plane.

---

## 14. Prop. I.35 — parallelograms on the same base

*(See Heath for the standard two-case proof using I.4 and the subtraction C.N. I.3.)* The key move is to observe that two parallelograms on the same base $BC$ and between the same parallels $BC$ and $AF$ have equal area because they can be built out of two triangles congruent to each other by I.4, plus or minus a common trapezium.

**Check.** Specializing to rectangles (one parallelogram being a rectangle on the same base and height), we recover the "base times height" formula — the link between Euclidean area and modern arithmetic.

---

## 15. Prop. I.47 — the Pythagorean theorem

**Setup.** Right-angled triangle $ABC$ with the right angle at $A$. Construct squares $BDEC$ on $BC$, $GFBA$ on $BA$, $AHKC$ on $AC$ (each by **I.46**).

**Construction.** Through $A$, draw $AL$ parallel to $BD$ meeting $BC$ at $M$ and $DE$ at $L$. Join $AD$ and $FC$.

**Demonstration.**

- $\angle DBC = \angle FBA = 90°$ (sides of squares). Adding $\angle ABC$ to both, by **C.N. I.2**: $\angle DBA = \angle FBC$.
- In triangles $DBA$ and $FBC$: $DB = BC$ (sides of square $BDEC$), $BA = BF$ (sides of square $GFBA$), $\angle DBA = \angle FBC$ (just shown). By **I.4**, $\triangle DBA = \triangle FBC$ (in particular, equal in area).
- Parallelogram $BDLM$ (on base $BD$, between parallels $BD$ and $AL$) is double $\triangle DBA$: by **I.41** (parallelogram on same base and parallels as a triangle is twice the triangle).
- Square $GFBA$ is double $\triangle FBC$: by the same **I.41** argument (both on base $FB$, between parallels $FB$ and $GC$, since $A$ lies on $GC$).
- Doubles of equals are equal: parallelogram $BDLM$ = square $GFBA$.
- Similarly, parallelogram $MLEC$ = square $AHKC$.
- Adding (**C.N. I.2**): $BDLM + MLEC = BDEC$ (the large square on the hypotenuse) equals $GFBA + AHKC$ (the sum of the squares on the two legs).

Hence the square on $BC$ equals the sum of the squares on $BA$ and $AC$. *Q.E.D.*

**Check.** The proof uses I.4 (superposition-based SAS), I.41 (triangle = half parallelogram on same base and parallels), I.46 (construction of a square on a given side), and I.47's own construction; every earlier step traces back to Post. 1–5 (especially Post. 5, *via* I.29 / I.31 / I.41). Specialize to a 3–4–5 triangle: the three squares have areas 9, 16, 25; indeed 9 + 16 = 25. Limiting case: as the right angle approaches a straight angle, the triangle degenerates; all three "squares" degenerate consistently.

---

## 16. Prop. I.48 — converse of Pythagorean

**Setup.** Triangle $ABC$ with $BC^2 = BA^2 + AC^2$; prove $\angle BAC = 90°$.

**Construction.** At $A$, erect $AD$ perpendicular to $AC$ (by **I.11**), with $AD = AB$. Join $DC$.

**Demonstration.**

- By construction, $\angle DAC = 90°$ and $AD = AB$. In right-angled triangle $DAC$: by **I.47**, $DC^2 = DA^2 + AC^2 = AB^2 + AC^2$.
- By hypothesis, $BC^2 = AB^2 + AC^2$.
- Hence $DC^2 = BC^2$, so $DC = BC$ (using **I.8** or by monotonicity of squaring on positive lengths).
- In triangles $ABC$ and $ADC$: $AB = AD$ (construction), $AC = AC$ (common), $BC = DC$ (just shown). By **I.8** (SSS), the triangles are equal in all respects; in particular $\angle BAC = \angle DAC = 90°$. *Q.E.D.*

**Check.** The converse genuinely requires I.47 in the proof, not only in the statement. Numerical sanity: $3^2 + 4^2 = 5^2$ implies the triangle with sides 3, 4, 5 has a right angle between the sides of length 3 and 4.

---

## 17. Playfair's axiom ⇔ Post. I.5

**(⇒)** Assume Post. I.5. Suppose through a point $P$ outside line $\ell$, two distinct parallels $m_1, m_2$ are drawn. Drop a transversal from $P$ to $\ell$ at $Q$. The alternate angles that $PQ$ makes with $m_1$ and with $\ell$ must sum to two right angles (since $m_1 \parallel \ell$, by the converse of I.28, or by a direct argument from Post. 5). Similarly for $m_2$. But $m_1 \neq m_2$, so the two angles at $P$ differ, and cannot both make two right angles with the angle at $Q$. Contradiction. Hence at most one parallel through $P$.

**(⇐)** Assume Playfair. Suppose a transversal makes interior angles $\alpha + \beta < 2$ right angles. We must show the lines meet. By the neutral theorem I.28, there *exists* a line through the transversal's intersection with one of the lines that is parallel to the other and makes interior angles summing to exactly two right angles. By Playfair that parallel is unique. Hence the original (different) line is *not* parallel, and — since we are in the plane — it must meet the other line. Finally, by I.16-style argument, it must meet on the side where the interior angles sum to less than two right angles. Hence Post. I.5.

**Check.** Each direction uses the other four postulates and Books I.1–I.28 (neutral geometry) but not Post. I.5 itself (in the reverse direction) or Playfair (in the forward direction). Both directions rely on I.28 as the crucial neutral hook.

---

## 18. Neutral-geometry boundary — two angles versus three

Produce $BC$ to $D$ (Post. I.2). By I.16, exterior angle $ACD$ exceeds opposite interior angle $ABC$. Add angle $ACB$ to both: $\angle ACD + \angle ACB > \angle ABC + \angle ACB$. The left side equals two right angles by I.13. Thus the selected two interior angles sum to less than two right angles; relabel the triangle for either other pair (I.17).

This uses preservation of inequality when the same magnitude is added, a principle Euclid uses without listing it among the common notions. No use of Post. I.5 occurs in these dependencies. I.32 concerns all three angles; its proof uses I.29, whose proof uses Post. I.5. It supplies an equality for the triple, not an equality for a pair. See [I.17](https://mathcs.clarku.edu/~djoyce/java/elements/bookI/propI17.html) and [I.32](https://mathcs.clarku.edu/~djoyce/java/elements/bookI/propI32.html).

**Check.** In an equilateral Euclidean triangle, a pair totals $120^\circ < 180^\circ$, while all three total $180^\circ$. The two statements are consistent.

---

## 19. Spherical counterexample to I.16

On the unit sphere, take a triangle whose three vertices are three points near the equator, with one vertex near the North Pole. The proof of I.16 constructs a midpoint $E$ of $AC$ and then a point $F$ "on the other side" of $BC$ equal in length to $BE$. On the sphere, "equal length" along a great-circle arc does not necessarily carry $F$ to the inside of the exterior angle; the arc bends around, and $F$ can end up on the far side. The exterior angle of a large spherical triangle can therefore fail to exceed a remote interior angle.

The broken assumption in Euclid's proof is that the line $BE$ produced beyond $E$ by a distance equal to $BE$ gives a point $F$ "on the other side of $BC$" — which depends on the underlying space being *flat and unbounded in the relevant direction*. On the sphere, lines are bounded (they close up after length $2\pi$), and the assumption fails.

---

## Exit-test outline (60 minutes, no references)

(a) Five postulates written out: check by comparing to the memorized list.
(b) Prop. I.1: two circles centered at $A$ and $B$, radius $AB$; intersection $C$; three radii all $= AB$; equilateral by C.N. I.1.
(c) Prop. I.5: extend; mark off equal lengths; apply I.4 twice; subtract common angles by C.N. I.3.
(d) Prop. I.47: construct squares on all three sides; draw $AL$ parallel to $BD$; by I.4, $\triangle DBA = \triangle FBC$; by I.41, parallelogram $BDLM$ = square $GFBA$; similarly for the other half; sum by C.N. I.2.

If all four tasks pass within the stated 60 minutes unaided, record the exit result and actual evidence in `learner-work.md`. Check the Book I box only when the remaining required learner work and dated learner-authored reflection also meet [the shared completion gate](../../../../docs/agents/tutoring.md#completion-gate). The existence of this reference outline is not assessment evidence.
