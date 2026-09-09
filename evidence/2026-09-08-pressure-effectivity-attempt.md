# Effective pressure bounds from the actual outer schedule

2026-09-08. S3040 / S008 / E004. Harness-only informal derivation.
Read with `INTEGRITY-CLAIMS.md`, `2026-09-08-source-certificate-attempt.md`
and `2026-09-08-effective-carrier-attempt.md`. No selected globally admissible
numerical field, completed positive-width certificate, Lean result or P=NP claim.

## Source identification and the dependency removed

Primary source inspected: [OpenAI, Finite time blowup for Navier--Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
Appendix A.2, equations (A.5)--(A.13), printed pp.129--130; Appendix A.4,
Lemma A.5, (A.21), printed pp.133--134. The pressure is

    Pi0(z) = -1/2 integral_R c(y)^2 f(z)^(2 theta(y)) dy,
    f(z) = 1/(1+z^2),                    0<=theta<=1.       (1)

Here c and theta are the actual unbumped radial schedule: the pressure-neutral
angular corrections are omitted. The inner segment has c=Pstar exp(y/10),
theta=1 for y<=0. The pressure does not require the pulse's axial amplitude
or later axis solution. Edits preserving the total pressure increment C_p
leave this datum unchanged.
It depends on outer choices but not the later radial scale XR.

The following bounds are derived here from these source formulas. They do
not select outer parameters; they work uniformly over schedules satisfying
the stated elementary slope conditions. Thus pressure holomorphy and upper
norm bounds need not wait for a complete numerical outer-cone certificate.

## A uniform integrable radial envelope

Let l=(log E)'+1/2, with differentiation in the global logarithmic radius y.
For the first unit interval, 0<=l<=3/5, so

    c(y)<=Pstar exp(y/10),             0<=y<=1.

After that interval the unbumped schedule has l<=0 at eta=0. This includes
the axial transition, negative-slope power laws and pulse. During the shape
interpolation, its eta=0 logarithm is

    log c = log e_end -(1/2+lambda)s -(1-theta(s))log 2;

theta decreases, so its last term cannot increase c. In the terminal stage
the prescribed bound f_o'/f_o<h/4 gives l<=-3h/4<0. Consequently

    c(y)<=Pstar exp(1/10) exp(-(y-1)/2),     y>=1.        (2)

These are bounds on the profile with the pressure-neutral angular bumps
omitted; bounding every later edited E this way is unnecessary and not claimed.
In particular, arbitrarily long finite intermediate intervals introduce no
factor proportional to their length. Integration gives

    integral_R c(y)^2 dy
      <= [5 + 2 exp(1/5)] Pstar^2 < 8 Pstar^2.           (3)

For the last strict inequality, the exponential series gives
exp(1/5)<=sum_k(1/5)^k=5/4<3/2. This is an exact rational estimate,
not decimal quadrature of a long pulse. It is uniform in the outer stage
durations and in the positive h,lambda values for which the slope bounds hold.

## One fixed complex domain and rational pressure majorants

Use the open rectangle

    Omega = { z : |Re z|<5/4, |Im z|<1/4 }.

For z=x+iy, Re(1+z^2)=1+x^2-y^2>15/16. Thus its principal logarithm is
holomorphic on Omega, and set f(z)^theta=exp(-theta Log(1+z^2)). Since
|z|<3/2, on this whole domain

    |f|<2,       |f'/f|=|2z/(1+z^2)|<4,
    |f^(2theta)|<=4,       |partial_z f^(2theta)|<=32.    (4)

The powers are defined by that single logarithm; theta is real. Equations
(2)--(4) supply integrable majorants independent of z. Uniform integration
therefore proves holomorphy of (1) and justifies its differentiated integral.
For ANY rational upper bound Pbar>=Pstar>0, sufficient rational certificates
on Omega are

    |Pi0| <= P0 := 16 Pbar^2,
    |Pi0'| <= P1 := 128 Pbar^2.                          (5)

This computes the two formerly unspecified pressure majorants from one outer
amplitude bound. No pressure quadrature, analytic-continuation oracle or
axis-field oracle is needed to prove (5).

The previous coefficient note used a complex r-neighborhood of
[-1-e,1+e], e<=1/1000 and r<=min(1/1000,sigma_axis^2/4096). Its closure
lies strictly inside Omega. Here sigma_axis is the Appendix B axis parameter,
not the smooth step in Appendix A. Hence (5) discharges that note's pressure
domain hypothesis and permits the explicit replacement

    Zbar = 192+10P0+6P1 = 192+928 Pbar^2.                 (6)

All later contraction and completed-tail obligations remain separate.

## Elementary schedule choices can also be made explicit

These choices certify the slope prerequisites above, not the full cone.
For the actual smooth step sigma of (A.5), a rational derivative bound is

    0<=sigma'<=128.

One verification is as follows. In 0<y<1, direct differentiation gives
sigma'=2 sigma(1-sigma)(y^-3+(1-y)^-3). On [1/4,3/4] this is at most
64. For 0<y<=1/4, sigma<=exp(2-y^-2)<9 exp(-y^-2), using e<3.
Writing v=1/y>=4, v^3 exp(-v^2)<=1 (the expression decreases for v>=4),
and (1-y)^-3<3. The derivative is therefore less than
18(1+3)=72. Reflection handles the other endpoint, and the flat extensions
have derivative zero. The larger bound 128 is convenient.

Thus one may take the fixed interpolation duration T_f=1280: in its formula
l=-lambda+theta'(log2-log(1+eta^2)), the parenthesis lies in [0,log2]
for eta in [-1,1], giving -lambda-1/10<=l<=-lambda.
Taking c_o=1/4096 in the terminal formula f_o=1-c_o h psi_o, with
0<h<=1/100 and psi_o=1-sigma((s-1)/2), gives f_o>1/2 and

    0<=f_o'/f_o <=128 c_o h = h/32 <h/4.

These are legitimate explicit values for two fixed schedule constants.
They select neither h nor lambda and make no claim that all the other
source smallness inequalities have been met. Similarly, given any rational
target epsilon_d>0, choosing an integer M_d>=512/epsilon_d ensures the
displayed axial step parameter e_d=4||sigma'||infinity/M_d<=epsilon_d.
The cone proof still has to supply a sufficient epsilon_d.

## Effective evaluation versus effective global admissibility

For a fixed effective outer schedule, (1) is computably evaluable with a
certified error. This claim includes the following representation requirement:
every fixed parameter and stage boundary must be given as a computable real
with an effective error procedure. It does not apply to arbitrary uncomputable
choices permitted by an existence theorem.

Given requested error epsilon>0, truncate y to [-R,R], R>=1. From (2)--(4)
the omitted pressure integral has absolute value at most

    10 Pbar^2 exp(-R/5) + 3 Pbar^2 exp(-(R-1)).            (7)

Indeed the left integral of c^2 is 5Pstar^2 exp(-R/5); the right is at most
(3/2)Pstar^2 exp(-(R-1)), and the pressure factor is at most two.
The same derivative-integral tail is bounded by eight times (7).
Choose an integer R by rational exponential enclosures until these strict
error tests pass. On the finite interval, evaluate the actual step, elementary
functions and integrated slopes with effective uniform errors, and use a
certified quadrature modulus. The fixed smooth step has explicit formulas,
flat endpoint bounds and computable derivative bounds; its rescalings have
effective moduli once their positive lengths are supplied. Composition and
finite integration consequently give the needed modulus for this finite
schedule. This supplies an algorithm, not a polynomial-runtime estimate.

The terminal waiting duration is not an arbitrary root oracle. Once the
preceding schedule is fixed, its Q value Q_in and the positive integral Q_p
in (A.13) are computable. If 0<Q_p<Q_in is certified and h<1, the constant
slope stage has duration log(Q_in/Q_p)/(1-h). Strict inequalities can be
verified by rational enclosures. Failure to establish their signs is an
unresolved schedule check, not permission to choose a negative wait.

The remaining outer selection cannot be replaced by just h=1/200. Explicit
first checks from the source include positive stage lengths, the strict
moment-contraction test 8 beta_k^2 kappa_k ||d||_(C^k)<1 for the required
finite derivative orders, and the two cone margins

    a-b_s w>0,
    2-2b_s w-b_s^2/a-(a-2)w^2>0,       Q_s>0.            (8)

Their source locations are Lemma A.2 (A.3) and (A.24). The pulse amplitude
equation (A.19) can be isolated constructively on [9/10,6/5] once its stated
C1 remainder is bounded by 1/100: the endpoint signs and positive derivative
then persist, and bisection plus that derivative bound is effective.

To select an actual instance, one still must bound those finite correction
operators/remainders and the cone margins in the correct order, first choosing
M_d and its associated T_d, then Pstar>exp(T_d), then lambda, then h.
Selecting an integer upper Pbar and an effective Pstar above exp(T_d) is
straightforward; certifying every subsequent required inequality is not
performed here. A dovetailed search over proposed parameters and interval
certificates is a possible method only AFTER the relevant compact-domain
moduli and endpoint-normalized strict tests have been constructed. The paper's
unspecified C_pre and asymptotic smallness statements are not themselves
passed effective tests, and this note does not assert that such a search
already terminates with a certified field.

## Updated boundary of this increment

The pressure radius and rational P0,P1 in the earlier source-certificate note
are no longer independent unknown inputs: (5) provides them on a uniform
domain for every schedule obeying the identified slope envelope. The same
actual pressure also has a concrete evaluation procedure once its effective
schedule is specified. The pressure construction does not depend circularly
on the later analytic-axis solution or completed flow.

The earliest remaining numerical dependency is full admissible outer parameter
selection, followed by the Appendix B axis choices, contraction remainder
bounds, and normalized higher-order/cutoff-tail bounds. Those are necessary
before claiming a positive-width completed-field carrier certificate. The
new pressure majorants improve that dependency chain without certifying the
entire source construction or changing the unresolved standard-model SAT
complexity obligation. No large numerical computation or simulation was used;
the discriminating evidence is the symbolic integrable envelope and complex
domain calculation above.
