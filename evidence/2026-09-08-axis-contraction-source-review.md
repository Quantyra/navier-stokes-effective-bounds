# Axis contraction source and effectivity review

2026-09-08. S3040 / S008 / E004. Baseline ba86f59. Independent harness-only review; no code, commits, planning edits or full-source certification.

## Primary-source anchors

The [Navier--Stokes manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), Appendix B, (B.4)--(B.16), printed pp.145--148, supplies the weighted coefficient space, degree-raising radial inverses and explicit remainders. Equations (B.14)--(B.15) define B=-2D eta A_X(u)-d partial_eta A_X(u), W=W_star+B/Lambda, H_c=H_star+du/Lambda, and p=I(g^2 Phi^2). Lemma B.1 bounds nonlinear derivative products after radial inversion. The inverse of 1+J_2 chi/2 is justified by factorial degree raising, not small operator norm. Proposition B.2's center is Phi0=f0(Y chi), u0=-Y Z_star/(2L). Equation (B.16) bounds g on a complex neighborhood after choosing C. This supplies uniform coefficient derivatives when Lambda is large. The real positivity margin is (B.11). Endpoint source/shear bounds in B.3 are additional claims.

## Independent enumeration and pitfalls

Expanding W and H_c gives three linear and seven quadratic terms in J_2 R1. The linear terms combine [W_star+h(1-2 eta U_star)]Phi, W_star D_Y Phi, H_star partial_eta Phi. Quadratics arise from two terms in B Phi, one in -2h eta u Phi/Lambda, one in d zeta_star u Phi, two in B D_Y Phi/Lambda, and one in d u partial_eta Phi/Lambda.

Similarly J_1 R2 has three linear terms, four quadratic terms and three pressure terms. The quadratics are -2A eta u^2/Lambda, the two terms in B D_Yu/Lambda, and d u partial_eta u/Lambda. The pressure terms are -4A eta p, d partial_eta p and -2 eta D_Yp. The pressure is quadratic in Phi for fixed g. This matches the author's announced enumeration.

Standalone parameter differentiation and logarithmic radial differentiation are not bounded operators on the same coefficient space. No estimate of an unintegrated R_i may be substituted for an estimate of J_nu R_i. In mixed products, the parameter and radial derivative act on distinct factors; radial averaging does not introduce a negative-degree singularity. Radial inverse outputs have zero constant coefficient, so the fixed-point correction preserves the prescribed axis values. The inverse series relies on chi preserving minimal radial degree and J_2 raising it.

## Uniformity and effectivity obligations

The center coefficients chi and Z_star/L must be fixed independently of Lambda and C. A common ball can then be chosen before Lambda. The family g changes with Lambda, but a bound on its larger complex domain after choosing C yields the same coefficient norm on the smaller domain. A real-axis bound alone would not control high derivatives and would leave a circular threshold argument. Lambda-dependent coefficient bounds hidden inside the proposed N or Lipschitz constant would likewise invalidate choosing Lambda last.

Rational majorants can give explicit finite parameter bounds once the outer/axis inputs and domain are fixed. They do not certify those inputs globally. A computable Picard convergence rate is not a polynomial bit-time theorem: effective coefficient evaluation, radial/parameter truncation and arithmetic costs must still be supplied. Very large constants fixed independently of SAT input size are not by themselves an asymptotic complexity lower bound; arbitrary real constants are not automatically effective data.

## Status

Source, term enumeration and final author artifact inspected. GO for the conditional local contraction and positivity bounds; INCOMPLETE for globally admissible source selection, endpoint continuation, completed-field certification and P=NP. Outer admissibility, axis separation, endpoint continuation and completed-field tails remain separate from this local contraction.


## Final candidate constants and effectivity lens

Read `2026-09-08-axis-contraction-effectivity-attempt.md` completely. The coefficient bound Bcoef=1000/sigma^2 covers the listed eta-only functions under the existing tube estimates and factor-three Cauchy conversion. In particular d zeta/L costs at most648/sigma^2; the axial linear coefficient stays below210. The integrated derivative estimate, with the extra coefficient multiplication, justifies T=a_alg Bcoef C_mix. No unintegrated derivative is silently treated as bounded.

For fixed g with norm at most3, the four-factor bound for g^2 Phi^2 is 9 a_alg^3 K^2. Its telescoped difference has bound18 a_alg^3 K times the input difference. Applying the three pressure operators and then the outer inverse/multiplication yields the stated 57600 a_alg^4 Bcoef(2+1/rho) coefficient. Adding the independently verified term counts gives N=T(6K+11K^2)+Pcoef K^2 and Lrem=T(6+22K)+2Pcoef K. These are bounds on the integrated remainders, with the max product norm bounded by the sum used in the formulas.

The choice Lambda>=8V(N+Lrem+1) yields both center displacement and Lipschitz constant at most1/16. The center, ball and uniform family bound for g are independent of the eventual Lambda. Choosing C on the larger complex tube supplies that bound after Lambda is fixed. This is not circular: each resulting contraction uses one fixed g, and the bound covers all allowed pairs. Increasing C later preserves it.

The zero-coefficient correction subspace is preserved by J_nu and by the angular inverse. The coefficient-to-value factor on Y<=4.1 is below4/3; a norm displacement1/16 therefore costs at most1/12. The external comparison bound above1/4 gives Phi>=1/6. The binomial coefficient envelope admits a common positive eta neighborhood on |Y|<=5; rho/4 is conservative. This checks a leading local analytic profile, not the endpoint shear or full completed field.

Effectivity clarification requested: radial coefficient truncation is not automatically small in the full B_rho weighted-supremum norm. A sequence can saturate that norm at arbitrarily high degrees. Exact Picard iterates nevertheless have the proved norm-geometric tail; coefficient envelopes give value and fixed-derivative truncation control on smaller compact domains. Finite-accuracy evaluation should refer to those outputs and explicitly cost coefficient/derivative access, rather than imply a norm-accurate finite representation of every iterate. No polynomial bit-runtime conclusion follows.

No mathematical correction to the fixed-point inequalities is needed. The formula-size description of a giant power of two is distinguished from the cost of writing all its binary digits or evaluating fields at requested precision. Local rational bounds and exact convergence improve the certificate chain; they do not fill in global parameter admissibility, separation, later continuation or normalized completed tails.

Follow-up verified: the final artifact now explicitly separates exact-iterate B_rho convergence from finite coefficient truncation for values/fixed derivatives on smaller analytic domains. The added coefficient-shift argument covers both omitted-derivative cases and alpha=0 without division by zero. The effectivity clarification is resolved. Final GO for the bounded conditional contraction remains; there are no outstanding review fixes.
