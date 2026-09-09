# Source coefficient certificate attempt

2026-09-08; S3040 / E004 / S008. Harness only. This is an informal derivation of explicit majorants for the actual Appendix B coefficient functions. It is **not a numerical instance of the completed flow**, a fluid device, or a P=NP proof. No globally admissible numerical h is selected.

## Source inspection and scope

I inspected the [primary manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), Appendix A (A.6), Appendix B (B.1)-(B.16), and the previous effective-carrier attempt and proof review. The schedule fixes h after the outer parameters, with additional smallness conditions. Appendix B then chooses axis data, a complex domain, a weighted coefficient space and a contraction. Its existence thresholds are not numerical input data. The following estimates replace several of those unnamed local majorants by explicit expressions; they do not replace the outer admissibility proof or completed-field tail bounds.

## Explicit domain for the rational coefficients

Fix any parameters in the necessary envelope 0<h<=1/100, 0<j<=1/20 and 0<sigma<=1. The last restriction can be imposed when making the source's small sigma choice. It is not a sufficient global admissibility condition. Set

    H(z)=(9/2-h)z-4z^3+j(1-z^2), L(z)=1-2hz^2,
    Q(z)=H(z)^2+sigma^2.

Let I=[-1-e,1+e], with 0<=e<=1/1000. For any rational radius

    0<r<=min(1/1000, sigma^2/4096),

write Omega_r for the open complex r-neighborhood of I. Its closure lies in |z|<101/100. The following estimates are uniform over **all** parameters in the stated envelope:

    |H|<9, |H'|<18, 1/2<|L|<2, |Q|>=sigma^2/2.

Indeed polynomial triangle estimates give the first three bounds. For z in the tube choose real x in I with |z-x|<=r. The segment is in the tube, and |(H^2)'|<324. Since Q(x)>=sigma^2,

    |Q(z)| >= sigma^2-324r >= (1-324/4096)sigma^2 > sigma^2/2.

With the source definitions chi=H^2/Q and zeta=-LH/Q, the actual coefficient functions satisfy

    |chi|=|H^2/Q|<=162/sigma^2,
    |zeta|=|LH/Q|<=36/sigma^2.

The tube is convex and simply connected, so zeta has an unambiguous primitive based at zero. The straight path from zero to z has length less than two. For every Lambda>=1,

    |phi_star(z)| = |exp(Lambda integral_0^z zeta)|
                 <= exp(72 Lambda/sigma^2).

Thus the **explicit** amplitude choice

    C = 2^ceil(144 Lambda/sigma^2)

ensures |g|=|phi_star/C|<=1 on this complex domain, because log(2)>1/2. On the real interval it also yields

    g >= 2^(-ceil(144 Lambda/sigma^2))/C > 0.

This lower bound is intentionally crude. It supplies a rational positive lower bound for the angular datum after Lambda,sigma have been selected, without numerical quadrature of the exponential. It proves no polynomial resource bound for C. Additional source amplitude thresholds may require increasing C; the bound then uses that larger C in its denominator.

The tube is a certified domain for H,L,Q,chi,zeta and phi_star. It is a domain for the **entire** Appendix B coefficient list only if the selected pressure datum Pi0 is holomorphic there. This pressure-domain hypothesis is not silently supplied by the calculation.

## Pressure majorants reduced to two numbers

Suppose that on this tube one has certified |Pi0|<=P0 and |Pi0'|<=P1, with nonnegative rational P0,P1. With U=4z+j, A=1/2+h and d=1-z^2, the prescribed Z expression gives

    |Z/L| <= 192+10P0+6P1 =: Zbar.

To check this, use |U|<5, |d|<3, |1-2zU|<12, A<1, |H U'|<36 and |4Az|<5. The four summands in Z have total magnitude at most 60+36+3P1+5P0, and |1/L|<2. This isolates the remaining pressure inputs instead of treating Z/L as an unspecified function norm.

For the coefficient norm of (B.4), choose rho=r/4. At any eta in I the disk of radius r/2 is inside the tube. If a coefficient a depends only on eta and has complex supremum at most M, Cauchy's bound yields

    ||a||_rho <= M sup_beta (beta+1)^2/2^beta <= 3M.

The sequence reaches 9/4 at beta=2 and decreases from there. Therefore

    ||chi||_rho <=486/sigma^2,
    ||zeta||_rho<=108/sigma^2,
    ||Z/L||_rho<=3 Zbar,  ||g||_rho<=3.

These are actual universal bounds for the displayed source coefficients, conditional only on the explicit pressure bounds and parameter choices, rather than evaluations of a synthetic flow certificate.

## Explicit operator constants

In the source convolution estimate, the elementary integral bound sum_{i>=1} i^-2<2 permits C_sq<16. Hence multiplication has norm at most 256. The proof of the mixed radial inverse estimate then gives the usable constant

    ||J_nu[(partial_eta F)(D_Y G)]||_rho
       <= (20480/rho) ||F||_rho ||G||_rho, nu=1,2.

Radial averaging can be inserted on F. Each extra undifferentiated factor costs a factor 256. The pure integrations obey ||J_nu||<=80 and ||partial_eta I||<=80/rho. These constants follow from the coefficient inequalities in the cited proof, retaining their endpoint indices.

Multiplication by chi is thus bounded by

    Mchi=124416/sigma^2.

For T=J_2 chi/2, the source degree-raising estimate and the exponential series give an explicit inverse majorant:

    ||(1+T)^-1|| <= sum_k (40Mchi)^k/[k!(k+1)!]
                  <= exp(40Mchi) <= 2^ceil(80Mchi) =: V.

No finite truncation of an oscillatory series is needed for that bound. The center of the contraction consequently has

    ||Phi0||<=V, ||u0||<=120 Zbar.

The latter uses u0=-Y Z/(2L) and ||Y a||<=80||a||. A unit ball about this center therefore has an explicit norm bound K=max(V,120Zbar)+1. This replaces the formerly unspecified center/ball size. It does not certify ball invariance: the explicit remainder monomials still need their bounds assembled, and Lambda must satisfy both invariance and Lipschitz inequalities.

## What remains before a positive-width certificate

Further update: `2026-09-08-axis-contraction-effectivity-attempt.md` now
assembles explicit norms N and Lipschitz bounds Lrem for the integrated
remainders, and gives finite Lambda/C choices proving local leading-profile
contraction under the stated local inputs. This resolves the unevaluated
contraction inequalities in item 3 below. Outer admissibility, axis separation,
continuation endpoint conditions and completed-field tails remain separate
obligations; a leading analytic coefficient certificate is not a completed
velocity certificate.

Update: `2026-09-08-pressure-effectivity-attempt.md` now resolves this note's
pressure-domain and P0/P1 dependency for the actual unbumped Appendix A
schedule under its stated slope conditions and a rational Pbar>=Pstar:
P0=16 Pbar^2, P1=128 Pbar^2 on a fixed complex rectangle containing this
note's tube. This supersedes that portion of item 2 below; outer admissible
selection, Appendix B separation/contraction, and completed-tail certificates
remain unresolved. The historical dependency list records the original attempt.

This attempt does **not** produce the requested completed numerical certificate. The following dependencies are still unresolved, in order:

1. Select the outer parameters satisfying all Appendix A smallness inequalities, not merely (A.6)'s order, and compute the resulting pressure datum. No admissible h=1/200 follows from this note.
2. Certify a pressure holomorphy radius and rational P0,P1. Select j,sigma satisfying the source's separation condition (B.2). The polynomial-denominator portion of the domain problem and the subsequent coefficient/amplitude bounds are now explicit above.
3. Assemble the remainder bounds N and Lipschitz bound Lrem on the stated ball using the displayed algebra constants. A sufficient contraction test is max(V,1) N/(2Lambda)<=1 and max(V,1) Lrem/(2Lambda)<1. These are named **unevaluated** inequalities, not passed checks. Further Appendix B continuation thresholds also remain.
4. Transfer the resulting leading norm bounds to the normalized completed field with explicit positive-order coefficient and cutoff-tail bounds, including the q derivative in radial velocity. A leading analytic solution alone is not the completed source construction.

The first unresolved numerical stage is therefore the outer schedule/pressure data, not the exponential primitive, rational denominator nonvanishing, Cauchy weight conversion, or angular inverse. Computing ever more decimal ticks would not supply those missing inputs. None of this supplies memory, external readout or a polynomial-bit-time SAT solver. The P=NP objective remains open.

## Verification

`check_source_coefficient_majorants.py` checks the universal rational polynomial bounds and coefficient-sequence envelope used above. Its inputs are worst-case ranges of the actual B.1 polynomials; it does not select an admissible instance or certify unknown PDE coefficients. The analytic arguments for complex nonvanishing, Cauchy estimates and operator convergence are written above and are not represented as numerical simulation tests.
