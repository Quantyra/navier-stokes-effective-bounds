# Explicit local axis contraction certificate

2026-09-08. S3040 / S008 / E004. Harness-only informal, source-dependent
derivation. This gives a conditional leading analytic coefficient certificate,
not a selected globally admissible completed flow, physical device or P=NP
result. Read `INTEGRITY-CLAIMS.md`, `2026-09-08-source-certificate-attempt.md`
and `2026-09-08-pressure-effectivity-attempt.md`.

## Inputs, source and intended result

The [primary manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
Appendix B.2--B.3, (B.4)--(B.16), printed pp.145--148, supplies the coefficient
space and rescaled integral equations. The nonlinear formulas below are its
explicit remainders, expanded before estimation. No external manuscript proof
or Lean build is independently certified by this note.

Assume fixed local inputs from the actual construction: rational
0<h<=1/100, 0<j<=1/20, 0<sigma<=1, a rational Pbar>=Pstar, and the actual
pressure datum Pi0. The preceding pressure note supplies its fixed complex
domain and norm bounds when the outer schedule satisfies the stated conditions.
Let e<=1/1000 and choose positive rational

    r<=min(1/1000,sigma^2/4096),       rho=r/4.

Use the same tube about I=[-1-e,1+e] as the source-coefficient note. Here sigma
is the axis separation parameter, not Appendix A's smooth step. Global outer
admissibility and the B.2 separation condition remain assumptions for the
intended source instance. The contraction calculation alone does not establish
the endpoint continuation/shear conclusions that use that separation.

Write A=1/2+h, D=1/2-h, d=1-eta^2, L=1-2h eta^2,
Ustar=4eta+j, Hstar=D eta+d Ustar, and use the source's Wstar,Zstar,zeta,chi.
All norms below are the weighted B_rho norm, with the product space carrying
the maximum norm. Radial averaging is denoted Av and D_Y=Y partial_Y.

## Constants available before Lambda is chosen

Use the conservative constants previously derived:

    a_alg=256,       J_bound=80,       Ieta_bound=80/rho,
    C_mix=20480/rho,                  ||Av||<=1,
    Zbar=192+928 Pbar^2,
    Mchi=124416/sigma^2,
    V=2^ceil(80 Mchi),
    K=max(V,120 Zbar)+1.

Here C_mix bounds J_nu[(partial_eta F)(D_Y G)], including either derivative
omitted, for nu=1,2. An extra undifferentiated factor costs one a_alg. The
operators J_nu,I,multiplication by Y have norm at most 80. V bounds the inverse
of 1+J_2 chi/2 by the factorial degree-raising series, NOT a small-operator
Neumann assumption. These constants have finite exponent representations;
none needs to be expanded into a gigantic integer to state the certificate.

Set the new coefficient bound and two convenient operator bounds

    Bcoef=1000/sigma^2,
    T=a_alg Bcoef C_mix,
    Pcoef=57600 a_alg^4 Bcoef (2+1/rho).                    (1)

Every eta-only coefficient explicitly listed in the next section has norm
at most Bcoef. To verify this, on the tube use |eta|<101/100, |d|<3,
|Ustar|<5, |Hstar|<9, |L^-1|<2, |Wstar|<19, |zeta|<=36/sigma^2,
and A<1,2D<=1. For an eta-only analytic coefficient the previous Cauchy
conversion multiplies its complex supremum by at most three. The largest
zeta-containing coefficient d zeta/L has norm at most 648/sigma^2.
The axial linear coefficient has norm below 210; all other listed coefficients
are smaller than 1000/sigma^2 by these bounds. For example
|A(1-4eta Ustar)+d Ustar_eta|<34 before division by L.
No derivative norm of an unknown field is claimed in this coefficient check.

The center is Phi0=f0(Y chi), u0=-Y Zstar/(2L). Its norms are at most
V and 120 Zbar. The closed unit ball about it therefore satisfies
||Phi||,||u||<=K. These constants are independent of Lambda and C.

## All nonlinear terms, before their radial inverses

Put epsilon=1/Lambda<=1, Q=g^2 Phi^2 and p=I Q, where g=phi_star/C.
The exact expansion of R1 is the sum of the following terms. Each listed
coefficient includes division by L:

| coefficient | unknown factors | multiplier |
|---|---|---|
| (Wstar+h(1-2eta Ustar))/L | Phi | 1 |
| d zeta/L | u Phi | 1 |
| Wstar/L | D_Y Phi | 1 |
| Hstar/L | partial_eta Phi | 1 |
| -2D eta/L | (Av u) Phi | epsilon |
| -d/L | (partial_eta Av u) Phi | epsilon |
| -2h eta/L | u Phi | epsilon |
| -2D eta/L | (Av u) D_Y Phi | epsilon |
| -d/L | (partial_eta Av u) D_Y Phi | epsilon |
| d/L | u partial_eta Phi | epsilon |

There are three linear and seven quadratic terms in the unknowns. The
corresponding R2 expansion is:

| coefficient | unknown expression | multiplier |
|---|---|---|
| [A(1-4eta Ustar)+d Ustar_eta]/L | u | 1 |
| Wstar/L | D_Y u | 1 |
| Hstar/L | partial_eta u | 1 |
| -2A eta/L | u^2 | epsilon |
| -2D eta/L | (Av u) D_Y u | epsilon |
| -d/L | (partial_eta Av u) D_Y u | epsilon |
| d/L | u partial_eta u | epsilon |
| -4A eta/L | p | 1 |
| d/L | partial_eta p | 1 |
| -2eta/L | D_Y p | 1 |

This has three linear, four quadratic, and three integrated-pressure terms.
It retains the derivative of the radial average inside W. In the mixed terms
the eta derivative and radial derivative act on distinct factor occurrences,
even when both factors depend on u. They are covered by the stated bilinear
estimate; no free boundedness of partial_eta or D_Y on B_rho is used.

Applying J_2 or J_1 first, each nonpressure linear term has norm <=T K,
and each nonpressure quadratic term has norm <=T K^2. The extra coefficient
cost a_alg is included in T. For a linear term, use the appropriate
derivative-omission estimate with the other, undifferentiated factor equal
to the constant 1, whose norm is 1. This does not differentiate the constant.
Averaging costs no extra factor.

For clarity, derivative omission here has a coefficient proof. At output
radial degree N=alpha+1, assign the raised degree to the eta-differentiated
factor of degree i. The weight-shift inequality (B.10) contributes at most
(80/rho)(i+1). The J_nu divisor is N(alpha+nu). With a radial derivative
on the other factor of degree alpha-i the extra ratio is
(i+1)(alpha-i)/[N(alpha+nu)]<=1; with that derivative omitted it is
(i+1)/[N(alpha+nu)]<=1. The two index convolutions cost at most256.
For J_nu[F D_Y G] without an eta derivative, (B.9) instead gives the
factor at most80(alpha-i)/[N(alpha+nu)]<=80, again with the two
convolutions. For J_nu[FG] it gives at most80/[N(alpha+nu)]. These
bounds are all at most C_mix since rho<1. Extra undifferentiated
coefficients are included by repeated convolution, as in the source proof,
not by pulling a coefficient through J_nu. This covers alpha=0: the
radial derivative then vanishes, while the omitted-derivative ratio is finite.

## Pressure terms and Lipschitz constants

After the amplitude choice below, ||g||<=3. Four-factor multiplication gives

    ||Q||<=9 a_alg^3 K^2,
    ||Q(Phi)-Q(Psi)||<=18 a_alg^3 K ||Phi-Psi||.

The second bound holds with the SAME fixed g for a fixed contraction problem.
Since p=I Q, partial_eta p=partial_eta I Q, and D_Y p=Y Q, their bounds are
80||Q||, (80/rho)||Q|| and 80||Q||. Applying the outer J_nu and multiplying
by each coefficient costs at most 80 a_alg Bcoef. Summing the three terms
therefore gives Pcoef K^2 with Pcoef in (1); their difference is bounded by
2 Pcoef K times the maximum input difference.

Thus explicit common norm and Lipschitz majorants for the pair
(J_2 R1,J_1 R2) on the unit ball are

    N=T(6K+11K^2)+Pcoef K^2,
    Lrem=T(6+22K)+2 Pcoef K.                               (2)

These use the sum of the two component bounds, which also bounds their
maximum. For differences, replace the two unknown factor occurrences one
at a time; each quadratic term contributes at most 2K. This includes p and
all averaged or differentiated products AFTER their indicated inverses.
N and Lrem bound the integrated remainders, not the potentially unbounded
maps R1,R2 themselves on this coefficient space.

## A finite noncircular selection and contraction proof

Choose an integer

    Lambda>=max(1,ceil(8 V (N+Lrem+1))).                    (3)

Then choose

    C>=2^ceil(144 Lambda/sigma^2).                         (4)

The prior primitive estimate bounds |phi_star| by exp(72 Lambda/sigma^2)
on the larger tube. Hence (4) gives |g|<=1 there. The same smaller-domain
Cauchy conversion yields ||g||<=3 uniformly in Lambda,C. Therefore the
bounds used to select Lambda really are independent of its later value:
g is a fixed coefficient for each chosen pair and is uniformly bounded
over the entire permitted family. If a later stage requires a larger C,
all the present estimates continue to hold.

The source fixed-point map is

    F(Phi,u)=(Phi0+(1+J_2 chi/2)^-1 J_2 R1/(2Lambda),
              u0+J_1 R2/(2Lambda)).

Since V>=1, equations (2)--(3) bound its distance from the center by
VN/(2Lambda)<=1/16 and its Lipschitz constant by
V Lrem/(2Lambda)<=1/16. It maps the closed unit ball into itself and is
a strict contraction. Banach's fixed-point argument provides a unique point
in that ball with norm distance <=1/16 from the center. Starting at the
center, the first displacement is <=1/16, and subsequent increments are
bounded by a geometric sequence of ratio 1/16. This gives an effective norm
error bound for exact Picard iterates; computational evaluation is discussed
separately below.

The affine subspace Phi(0,eta)=1,u(0,eta)=0 is preserved. Both J inverses
produce zero constant radial coefficient. The angular inverse preserves
that zero coefficient because every occurrence of J_2 chi raises radial
degree; its identity term also preserves zero. Thus the fixed point has
the intended regular axis data, without imposing a hidden nonzero mode.

For beta=0 the coefficient envelope gives
|F(Y,eta)|<=||F||/(1-|Y|/20). At 0<=Y<=41/10 the bound is less than
(4/3)||F||. The source comparison satisfies f0(Y chi)>1/4 on this real
interval, because 0<=chi<=1 and (B.11) applies. Our norm error <=1/16
therefore implies

    Phi>=1/4-1/12=1/6>0.                                  (5)

Division by phi=phi_star Phi in the source angular equation is valid on
the real rectangle. The coefficient series converges on |Y|<=5 with a
positive common eta neighborhood; one may choose eta displacement less
than rho/4 using the coefficient binomial sum. Therefore this is a
positive-width leading analytic profile on 0<=X<=41/(10Lambda), with
real coefficients by iteration from the real center. It is not a bound
on the completed cutoff sum or the continuation endpoint shear margin.

## Effectivity and remaining source obligations

Equations (1)--(4) are explicit finite upper bounds and selection rules in
the local input certificate. They replace the previously unevaluated
remainder norm and Lipschitz inequalities. Given effective representations
of the actual pressure and fixed parameters, elementary coefficient operations,
radial integration and the factorial inverse series have effective truncation
errors for values and any fixed derivatives on smaller compact analytic
domains. The Picard geometric tail controls the exact iterates in B_rho;
the coefficient envelope converts that error to these evaluation errors.
Finite coefficient truncation need NOT converge in the full B_rho norm:
its weighted supremum tail can remain nonzero. No norm-accurate finite
truncation oracle is assumed. These two distinct error controls provide
finite-accuracy access to the local solution on smaller domains. Such an implementation
must also bound rounding, coefficient truncation and differentiated evaluations;
none is counted as a free oracle or implemented in this note.

In particular, logarithmically many exact Picard iterations for a requested
norm error is not a polynomial-bit-time theorem: each iterate is an analytic
object and the cost of its representation and evaluation matters. Fixed giant
constants, precision-dependent truncation, and SAT-input-dependent parameters
have different resource roles and cannot be conflated.

No earlier coefficient constants needed correction in this calculation.
The full admissible outer choice, the Appendix B separation data, and later
continuation thresholds must still be supplied for a particular source field.
Most importantly, a leading analytic profile is not the completed velocity:
positive-order coefficients, cutoff derivatives, and uniform normalized tails
remain necessary for the finite carrier rectangle. This local contraction
does not establish those facts, programmable fluid hardware or a polynomial
SAT computation. The overarching P=NP objective remains unresolved.
