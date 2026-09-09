# Axis contraction: proof and nonclaims review

2026-09-08. S3040 / S008 / E004. Baseline `ba86f59`.
Harness only. One independent reviewer covers the two separately reported
lenses; these are not two separately staffed reviews. Another reviewer audits
source alignment. No code, formal module/build, commit, planning edit or
publication is part of this review.

Reviewed stable `2026-09-08-axis-contraction-effectivity-attempt.md`, including
the added derivative-omission argument and the distinction between coefficient
norm convergence and smaller-domain evaluation. Read its preceding pressure
and source-coefficient dependencies. Independently opened the [primary
manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
at the Appendix B weighted norm, radial bounds, remainders and inverse map.

## Proof-adversarial lens: GO for the conditional local analytic certificate

**Equation audit.** Expanding W=Wstar+Lambda^-1(-2D eta Av(u)-d partial_eta Av(u)),
U=Ustar+Lambda^-1 u, and Hc=Hstar+Lambda^-1 du reproduces all ten angular
rows: three linear and seven quadratic unknown terms. The axial expansion
contains three linear, four quadratic, and three pressure terms. In particular
the derivative of Av(u), the epsilon u partial_eta u term, and all three
pressure contributions are retained. Coefficients multiplying differentiated
unknowns are estimated with their own eta dependence; no unknown derivative
is treated as a bounded stand-alone operator on B_rho.

**Derivative operators.** The initial text needed an explicit justification
for omitting derivatives from the mixed-product bound. The final revision
provides it. At radial output degree N=alpha+1, the eta-derivative weight shift
on input degree i contributes at most (80/rho)(i+1). The inverse divisor
N(alpha+nu) bounds both the eta-only ratio and the mixed ratio with the
additional factor alpha-i. The radial-only estimate instead uses the ordinary
weight shift, contributing at most 80(alpha-i)/[N(alpha+nu)]. Plain products
are easier. Two convolution constants give 256. These estimates hold also at
alpha=0; a radial derivative there vanishes. Linear terms use an
undifferentiated constant factor, not the false assertion that its derivative
is one. Averaging has norm at most one. Extra coefficient convolutions cost
the stated algebra factor. Thus C_mix=20480/rho covers the required operators.

**Coefficient and center bounds.** The eta-only Cauchy conversion is a factor
at most three. The largest displayed zeta coefficient is bounded by
648/sigma^2; the axial linear coefficient is below 210. Bcoef=1000/sigma^2
therefore covers the table. The center has norms at most V and 120 Zbar, so
the unit ball lies in the maximum-norm K bound. The factorial radial-degree
inverse establishes V without assuming that the order-one angular operator
has norm below one. Multiplication by chi preserves lower radial degree and
J raises it, as needed in this inverse argument.

**Pressure and differences.** With one fixed g per problem and ||g||<=3,
four-factor multiplication gives ||g^2 Phi^2||<=9 a_alg^3 K^2. Replacing its
two variable occurrences one at a time gives the difference bound
18 a_alg^3 K delta. For p, partial_eta p and D_Y p, the operators are I,
partial_eta I and multiplication by Y, respectively. Applying their bounds
before the outer J and coefficient multiplication gives
80*80*9 a_alg^4 Bcoef (2+1/rho), precisely Pcoef. In particular the derivative
pressure term uses the integrated derivative estimate, not an unbounded
parameter derivative. The same fixed-coefficient treatment doubles the
quadratic difference coefficient.

Summing the two component estimates gives the declared conservative common
N=T(6K+11K^2)+Pcoef K^2 and Lrem=T(6+22K)+2 Pcoef K. Taking the sum instead
of the maximum is harmless. These bound the integrated remainders, not the
bare differential remainders.

**Noncircular selection.** All displayed majorants are fixed before Lambda.
After selecting Lambda, increasing C supplies a uniform larger-domain bound
on g, and hence the same ||g||<=3 for every allowed pair. No derivative with
respect to Lambda is part of the Lipschitz problem. This makes the use of
N,Lrem in Lambda>=8V(N+Lrem+1) legitimate. The map displacement and Lipschitz
constant are each at most 1/16; the closed unit ball is invariant and complete.
The fixed point itself therefore lies within 1/16 of the center. The geometric
Picard increment bound follows.

**Axis data, positivity and domain.** Both J maps produce zero constant radial
coefficient. The angular inverse preserves that subspace termwise, so the
map has the correct affine radial-zero data. On 0<=Y<=4.1, the beta=0
coefficient envelope gives an evaluation factor below 4/3. The source's
comparison lower bound, combined with the 1/16 norm error, gives
Phi>=1/4-1/12=1/6. Division by the positive angular profile is thus justified
on the real rectangle. At |Y|<=5 the binomial coefficient sum and eta
displacement below rho/4 give convergence with a strict geometric margin,
and therefore a common analytic neighborhood. Real iteration preserves real
coefficients. None of these arguments gives the later shear or completion
tail margins.

**Effectivity.** The revised statement correctly separates exact Picard
convergence in B_rho from finite evaluation on smaller analytic domains.
Finite coefficient truncations need not approximate in the full weighted
supremum norm. No such approximation oracle is assumed. Effective pressure
and parameter data, analytic tails and factorial inverse tails give
conditional finite-accuracy local evaluation; they do not establish its
polynomial complexity or constitute an implemented evaluator.

No blocking mathematical defect remains after the derivative-omission
clarification. This is a reviewed informal implication from the stated local
inputs and preceding coefficient bounds, not an independent certification of
the entire manuscript.

## Nonclaims lens: GO-WITH-NOTES for bounded exploratory use

The result explicitly supplies a conditional local leading-axis contraction
rule and analytic interval. Its adjective "positive-width" refers to that
leading profile only. It must not be shortened in summaries to a completed-flow
carrier certificate. Full admissible outer selection, source separation,
continuation thresholds, positive-order corrections and cutoff tails remain
unresolved and are named in the draft.

The huge finite constants are descriptions of sufficient bounds, not a
polynomial runtime result. The number of exact Picard iterations is not
confused with the work needed to represent/evaluate each analytic iterate.
No physical sensor, programmable bit, external readout, SAT algorithm or
P=NP conclusion follows from this contraction.

Safe summary: previously unnamed local integrated-remainder bounds are now
explicit, giving a noncircular Lambda-then-C rule for the conditional leading
analytic axis problem; completed source-field and computational obligations
remain open. No stronger claim expansion or full-goal completion is approved.
