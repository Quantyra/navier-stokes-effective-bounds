# Pressure source dependency and effectivity review

2026-09-08. S3040 / S008 / E004. Baseline 6bfed2f. Independent harness-only source/effectivity lens. No code, commits, planning edits or full-PDE certification.

## Source identification and dependency order

The [primary Navier--Stokes manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), Appendix A.4 Lemma A.5, equations (A.21)--(A.23), printed pages 133--134, defines the axis pressure as minus one-half the logarithmic-radial integral of the squared scheduled reference swirl. Angular corrections preserving total pressure increment are omitted. The remaining profile has E=c(y)f(eta)^theta(y), with f=(1+eta^2)^(-1), 0<=theta<=1, and c,theta independent of eta. Later moment-preserving edits do not alter this datum. The logarithmic-coordinate construction makes it independent of X_R.

Appendix A.2, (A.6)--(A.12), fixes the outer schedule before Appendix B.1 uses this pressure. Its order is M_d, T_d, P_star, lambda, then h; h has additional smallness requirements. Appendix B next selects j, separation data and sigma, a complex domain, Lambda and C. The pressure need not be extracted from the completed fluid or solved axis profile. It may depend on the outer schedule and h even though X_R drops out. Real analyticity is not a claim that every later smooth correction admits the same complex continuation.

## Independent bound checks before the final candidate

Read the existing `2026-09-08-source-certificate-attempt.md`; its pressure-domain and P0,P1 assumptions are explicit. The new attempt targets those assumptions rather than an arbitrary synthetic pressure.

For the scheduled, unbumped amplitude c(y)=E(y,0), the inner interval contributes exactly 5 P_star^2 to integral c^2. On the first unit interval, logarithmic amplitude slope l-1/2 is at most 1/10. Thereafter the specified unbumped stages have l<=0: the axial and intermediate stages, pulse, interpolation, exterior transitions and terminal collar all satisfy this sign when their stated parameter inequalities hold. The interpolation's additional constant-factor transition does not create growth. The pulse's adjustable amplitude changes axial U, not this unbumped swirl. Thus

    c(y)<=P_star exp(1/10),                 0<=y<=1,
    c(y)<=P_star exp(1/10) exp(-(y-1)/2),   y>=1,
    integral_R c(y)^2 dy <= (5+2 exp(1/5)) P_star^2 < 8 P_star^2.

This is an independent sufficient envelope; long radial stage lengths do not force a large integral because the amplitude decays. Pressure-preserving angular bumps must remain omitted in this estimate. Later actual edits are reconciled through the pressure-increment identity, not by asserting the same pointwise c bound for every edited field.

On the proposed rectangle |Re z|<5/4, |Im z|<1/4, Re(1+z^2)>15/16. Hence 1+z^2 remains in the right half-plane, permitting its principal logarithm. Its inverse f has |f|<2 and |f'/f|<4. For every real theta in [0,1], the analytic branch f^(2theta) therefore has modulus at most 4 and derivative modulus at most 32. The integrable c^2 envelope uniformly dominates both integrands. The pressure bounds P0=16 Pbar^2 and P1=128 Pbar^2 follow for rational Pbar>=P_star. These numbers are sufficient uniform bounds, not pressure values or global admissibility certificates.

## Effectivity and circularity checks

A symbolic majorant parameterized by Pbar can close a previously unnamed local estimate without selecting a globally admissible numerical instance. That is real progress, but the distinction must remain explicit. To produce numeric bounds, supply a certified rational Pbar covering the selected amplitude. To compute pressure values to arbitrary accuracy additionally requires effective schedule coefficients, branch choices and an integration algorithm with an error bound. To assert polynomial evaluation requires a uniform bit-work theorem for those operations; existence, analyticity and a fixed constant do not automatically supply it.

If all schedule constants are fixed independently of SAT input length, their magnitude is not itself input asymptotic complexity. Their effective representation still matters: unspecified or noncomputable real advice cannot be justified merely by calling it fixed. If constants vary with requested accuracy, cutoff or formula, that dependence must be counted explicitly.

Computing this pressure from the pre-axis schedule avoids circular dependence on the unknown axis solution. It does not select j/sigma satisfying separation, prove contraction, bound the completed remainder or produce a uniform finite-dimensional SAT simulator. The final source field and P=NP remain unproved by this local result.

## Status

Primary source and final author artifact inspected. GO for the conditional pressure-domain, majorant and effectivity derivations; INCOMPLETE for a globally admissible numerical source instance, completed carrier certificate and P=NP. This reviewer does not independently certify the entire external manuscript or completed PDE construction.


## Final author-artifact review

Inspected `2026-09-08-pressure-effectivity-attempt.md` in full. The envelope, common logarithm, differentiation under an integrable majorant, pressure norm bounds and substitution Zbar=192+928 Pbar^2 are valid. The small previous coefficient tube lies strictly inside the rectangle. These are universal sufficient bounds conditional on the specified stage signs and amplitude upper bound; no pressure evaluation or selected axis field is used in their proof.

The explicit step derivative bound is conservative and valid: differentiation gives 2 sigma(1-sigma)(y^-3+(1-y)^-3); the middle and endpoint estimates cover its support, and reflection covers the other endpoint. Consequently T_f=1280 gives the stated interpolation slope bound on the real parameter interval. The terminal choice c_o=1/4096 together with 0<h<=1/100 bounds f_o away from zero and gives f_o'/f_o<=h/32. These choices certify only the named slope conditions, not all outer-cone smallness conditions.

The two tails in equation (7) correctly include the one-half pressure factor, complex-power majorant and radial envelope. The derivative tail is at most eight times that bound. Given effective positive stage lengths and parameters, the finite-interval quadrature procedure has effective moduli; the note does not claim polynomial runtime. The terminal waiting-time formula follows from the constant-slope ODE Q'=-(1-h)Q and is conditional on a certified strict ratio. The pulse root bracket likewise requires the stated remainder bound before bisection can certify a root. These qualifications prevent circular use of an unverified schedule.

This audit identifies the function as the Appendix A.21 datum used in B.1. It does not certify the complete physical pressure, any separate correction field, or completed asymptotic remainder. No evidence of an additional correction was needed for the local statement, and no hypothetical correction is assumed away in a global claim.

No source-dependency, complexity or effectivity correction is required. The conditional pressure-domain and P0,P1 dependency is discharged by explicit formulas; globally admissible parameter selection, separation, contraction and completed-field estimates remain open. Final verdict: GO for this bounded informal increment; INCOMPLETE for the completed numerical source and standard-model SAT bridge. No code, commits or planning changes were made by this reviewer.
