# Pressure effectivity: proof and nonclaims review

2026-09-08. S3040 / S008 / E004. Baseline `6bfed2f`.
Harness only. One reviewer covers the two separately reported lenses below;
these are not two independently staffed reviews. A separate source reviewer
checks manuscript alignment. No code, formal modules/builds, commits, planning
edits, or publication are part of this review.

Reviewed stable `2026-09-08-pressure-effectivity-attempt.md`, including the
clarification that only edits preserving the total pressure increment C_p
leave this datum unchanged. Also read the earlier source-coefficient note.
Independently opened the [primary manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
checking A.5--A.13, A.19, A.21, A.24 and Lemma A.2 as used here.

## Proof-adversarial lens: GO for the stated conditional bounds

The manuscript's A.21 datum omits the pressure-preserving azimuthal edits and
uses the reference inner profile followed by the outer schedule. The order of
outer parameter choice precedes the analytic-axis construction. Axial pulse
amplitude does not enter the unbumped E datum. This matches the reviewed
integral; it is not a formula asserted for the entire completed physical
pressure. No additional finite-order correction hypothesis has been supplied
or needed for the displayed A.21 calculation.

**Radial envelope.** In global logarithmic radius, c'/c=l-1/2 at eta=0. The
first interval gives c<=Pstar exp(y/10). Every following unbumped segment has
l<=0, including the decreasing profile interpolation and the terminal stage.
Integrating gives (2). The negative half-line contributes exactly 5 Pstar^2
to integral c^2; the first positive unit contributes at most exp(1/5)Pstar^2,
and the remaining tail at most the same. Therefore (3) follows. The geometric
series bound exp(1/5)<=5/4 gives a strict upper bound below 8 Pstar^2.
Long intermediate durations do not add an uncontrolled factor.

**Complex domain.** On the chosen rectangle, Re(1+z^2)>15/16. The principal
logarithm is single-valued there, with |f|<2 and |f'/f|<4. Since theta is real
and lies in [0,1], |f^(2theta)|<=4 and its z derivative is at most 32.
The radial majorant is integrable and independent of z. Dominated holomorphic
integration and differentiation are therefore justified, giving P0=16Pbar^2
and P1=128Pbar^2. The earlier small tube lies strictly within this rectangle.
Substitution gives 10*16+6*128=928 in Zbar. These statements need an upper
Pbar for the schedule amplitude, not pressure quadrature or an axis solution.

**Explicit schedule constants.** Differentiating the stated step gives
2 sigma(1-sigma)(y^-3+(1-y)^-3). On the middle half, the crude bound 64 is
valid. On the left quarter the exponential tail gives less than 72; reflection
handles the right quarter. Flat endpoints have derivative zero. Thus 128 is
safe. With T_f=1280, |theta'|<=1/10 and the interpolation logarithm multiplier
lies in [0,log 2], proving the chosen slope interval. With c_o=1/4096 and
h<=1/100, f_o>1/2 and f_o'/f_o<=128 c_o h=h/32<h/4. The M_d bound follows
directly from 4*128/M_d. None of these checks selects sufficient cone margins.

**Effective pressure evaluation.** The omitted pressure tails are bounded
by (7); the derivative integrand estimate differs by a factor eight. Searching
integer truncation radii with rational exponential bounds terminates for every
positive error request and fixed effective Pbar. A finite, effectively given
schedule has computable compact-interval moduli: the fixed step, its positive
rescalings, elementary functions and integrated slopes allow certified
quadrature. The explicit representation assumption on all parameters and
stage boundaries is indispensable and present. Computability is established
conditionally, without a polynomial cost estimate or an evaluator for
unspecified arbitrary real choices.

**Remaining parameter choices.** On l=-h, the stated Q equation reduces to
Q'=-(1-h)Q. Hence a positive wait from Q_in to Q_p is precisely
log(Q_in/Q_p)/(1-h), provided 0<Q_p<Q_in and h<1. These strict hypotheses are
not silently presumed verified. The A.19 principal bracket has the source's
opposite endpoint signs and derivative at least 0.36; a C1 remainder at most
0.01 retains endpoint gaps and derivative at least 0.35. Effective isolation
by interval evaluation with this derivative bound is valid, conditional on
actually certifying that remainder. The note does not claim that certification.

The strict version of the moment smallness test is a sufficient strengthening
of the source's non-strict test. The cone tests, positive stage lengths,
finite correction norms and subsequent axis/tail bounds remain separate.
There is no circular dependence on the later axis solution in the new pressure
majorants. No blocking defect was found in these bounded derivations.

## Nonclaims lens: GO-WITH-NOTES for bounded exploratory use

The advance is explicit holomorphy and norm bounds for the identified A.21
pressure datum, plus conditional effective evaluation once its schedule is
specified. It removes those particular unnamed pressure-bound inputs from the
earlier dependency list. It does not instantiate globally admissible numerical
outer parameters or certify a completed positive-width carrier.

The manuscript is a named external source, not independently certified here.
The note retains the unpassed outer cone/moment checks, Appendix B contraction
remainders, higher-order completion and cutoff tails. A hypothetical interval
search is not presented as already implemented or proved terminating with a
certified field. Large finite or computable constants are not treated as
polynomial-time bounds.

The requested clarification about pressure-preserving edits was applied and
verified before this verdict. It prevents a claim about arbitrary edits that
preserve other moments. There is no evidence requiring an additional finite-M
pressure term in this A.21 calculation, and none has been invented.

Safe closeout wording: actual-source pressure majorants and a fixed complex
domain are now explicit, conditional on the stated outer schedule envelope
and amplitude bound; full effective admissibility and completed-flow data
remain unresolved. No fluid device, general SAT capability, P=NP conclusion,
or claim-boundary expansion is approved. No finite numerical simulation was
needed or represented as evidence for the analytic result.
